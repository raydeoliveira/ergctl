---
name: ergctl
description: Control and coach Bluetooth SIG FTMS and Concept2 PM5 fitness ergometers over CLI, bidirectional NDJSON stream, or stdio MCP 2024-11-05.
---

# Agent Guide for ergctl

Always inspect capabilities and dry-run before sending live hardware targets:

1. **Discover manifest & machines**:
   ```bash
   ergctl --describe
   ergctl probe --sim --json        # or --transport ble | usb
   ```
   Check `capabilities.electronic_resistance`, `supports_power_target`, `supports_speed_target`, `supports_incline_target`, `supports_bike_simulation`, and `supported_ranges`. Note Concept2 PM5 air ergs set `electronic_resistance: false` and `programmable_target_display: true`.

2. **Safe dry-run before live mutation**:
   Pass `--dry-run --yes --json` on CLI or omit `dry_run: false` on MCP mutating tools (every mutating MCP tool except `erg_connect`/`erg_disconnect` defaults to `dry_run: true`).

3. **Live Bidirectional Coaching Stream**:
   Launch `ergctl stream --device <id> --rate-ms 250 --json --bidirectional`.
   - Read monotonic NDJSON events (`schema_version: 1`, `seq`, `ts`, `type`, `data`).
   - Send one-line JSON commands on stdin:
     - `{"command":"set_target_power","watts":220}`
     - `{"command":"set_target_speed","kph":11.5}`
     - `{"command":"set_target_incline","percent":4.0}`
     - `{"command":"set_target_resistance","level":10.0}`
     - `{"command":"set_bike_simulation","wind_speed_mps":0.0,"grade_percent":5.0,"crr":0.004,"cw_kg_per_m":0.51}`
     - `{"command":"coach_cue","text":"Hold 24 spm","urgency":"nudge","ttl_seconds":8}`
     - `{"command":"pause"}` / `{"command":"resume"}` / `{"command":"stop"}`
   - When `ERGCTL_WATCHDOG_MS` is set, send periodic commands/cues before timeout or `ergctl` reverts targets to baseline and emits `WATCHDOG_REVERT`.

4. **MCP Server (`ergctl mcp`)**:
   Implements JSON-RPC 2.0 `2024-11-05` on stdio:
   - **16 tools**: `erg_probe`, `erg_connect`, `erg_disconnect`, `erg_telemetry`, `erg_poll_events`, `erg_set_target_power`, `erg_set_resistance`, `erg_set_speed`, `erg_set_incline`, `erg_set_simulation`, `erg_start_workout`, `erg_pause`, `erg_resume`, `erg_stop`, `erg_coach_cue`, `erg_export_session`.
   - **4 resources**: `erg://device/capabilities`, `erg://telemetry/live`, `erg://workout/active`, `erg://session/summary`.
