#!/usr/bin/env python3
"""Minimal live AI-coaching feedback loop driving `ergctl stream --bidirectional`.

Key API: run_coach_loop(binary, device_id, max_ticks, target_watts)
Core Invariant: Reads monotonic NDJSON telemetry and issues bounded target/cue updates under watchdog supervision.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys


def send_cmd(proc: subprocess.Popen[str], payload: dict[str, object]) -> None:
    """Write one newline-delimited JSON command to ergctl stdin."""
    if proc.stdin is None:
        return
    proc.stdin.write(json.dumps(payload) + "\n")
    proc.stdin.flush()


def run_coach_loop(binary: str, device_id: str, max_ticks: int, base_watts: int) -> int:
    """Spawn ergctl stream, adapt watts from live heart rate/power, and stop cleanly."""
    env = dict(os.environ)
    env.setdefault("ERGCTL_WATCHDOG_MS", "3000")
    cmd = [binary, "stream", "--sim", "--device", device_id, "--rate-ms", "250", "--json", "--bidirectional"]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, env=env)
    telemetry_seen = 0
    current_target = base_watts

    assert proc.stdout is not None
    try:
        send_cmd(proc, {"command": "set_target_power", "watts": current_target})
        send_cmd(proc, {"command": "coach_cue", "text": f"Lock {current_target}W steady cadence.", "urgency": "info"})

        for raw_line in proc.stdout:
            line = raw_line.strip()
            if not line:
                continue
            event = json.loads(line)
            ev_type = event.get("type")
            data = event.get("data") or {}
            if ev_type == "telemetry":
                telemetry_seen += 1
                hr = data.get("heart_rate_bpm")
                pwr = data.get("instantaneous_power_watts")
                print(f"[tick {telemetry_seen:02d}] power={pwr}W target={current_target}W hr={hr}", file=sys.stderr)
                if hr is not None and hr >= 165 and current_target > 140:
                    current_target -= 15
                    send_cmd(proc, {"command": "set_target_power", "watts": current_target})
                    send_cmd(proc, {"command": "coach_cue", "text": f"HR high ({hr} bpm) -> ease to {current_target}W", "urgency": "nudge"})
                elif telemetry_seen % 4 == 0:
                    send_cmd(proc, {"command": "coach_cue", "text": f"On target at {current_target}W", "urgency": "info"})
                if telemetry_seen >= max_ticks:
                    send_cmd(proc, {"command": "stop"})
                    break
        rc = proc.wait(timeout=5)
        return rc
    finally:
        if proc.poll() is None:
            proc.terminate()
            proc.wait(timeout=5)


def main() -> int:
    parser = argparse.ArgumentParser(description="Live AI coaching feedback loop example for ergctl.")
    parser.add_argument("--bin", default="ergctl", help="Path to ergctl binary")
    parser.add_argument("--device", default="sim-ftms-bike-1", help="Device ID (simulator or probed hardware)")
    parser.add_argument("--ticks", type=int, default=8, help="Telemetry samples before stopping")
    parser.add_argument("--watts", type=int, default=200, help="Initial target power in watts")
    args = parser.parse_args()
    return run_coach_loop(args.bin, args.device, args.ticks, args.watts)


if __name__ == "__main__":
    raise SystemExit(main())
