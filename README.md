# Ergctl

> **Product Hub:** [raymonddeoliveira.com/software#ergctl](https://www.raymonddeoliveira.com/software#ergctl) · **Buy Ergctl Pro ($29):** [Polar Checkout](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT) · **Releases & Checksums:** [GitHub Releases](https://github.com/raydeoliveira/ergctl/releases) · **Verified MCP:** [Glama](https://glama.ai/mcp/servers/raydeoliveira/ergctl) · **Official MCP Registry:** [io.github.raydeoliveira/ergctl](https://registry.modelcontextprotocol.io/v0.1/servers?search=raydeoliveira/ergctl) · **Free Core:** `brew tap raydeoliveira/tap && brew install ergctl`

Zero-dependency macOS CLI, interactive terminal dashboard (`tui`), structured workout engine, and live `--json` / MCP AI-coaching controller for **Bluetooth SIG FTMS v1.0 (`0x1826`)** and **Concept2 PM5 (`CE06xxxx` BLE GATT + `VID 0x17A4` USB HID CSAFE)** fitness ergometers.

Replaces **$20–$44/mo** closed trainer and indoor rowing subscriptions with one native **~1.9 MB** Apple Silicon binary — 100% open protocols, zero proprietary SDKs, zero reverse-engineering risk, binary `.fit` export (CRC-16), and a live bidirectional AI-coaching loop.

## Measured Footprint

Measured on Apple Silicon (`arm64-apple-macos14.0`, Swift 6.4.2):

| Metric | Measured Value |
|---|---|
| Stripped binary (`arm64`) | `1,987,952 bytes` (`1.90 MiB`) |
| Compressed release tarball (`.tar.gz`) | `~753 KB` (`0.72 MiB`, binary + docs + MCP manifest) |
| Claude Desktop bundle (`.mcpb`) | `~756 KB` (`0.72 MiB`, signed binary + MCP manifest + docs) |
| External runtime dependencies | `0` (Swift stdlib, Foundation, CoreBluetooth, IOKit, Darwin) |
| `--version` latency (10 subprocess runs) | `13.38 ms` median (`10.00–18.22 ms`) |
| Automated verification | `57` XCTests + `208` Python E2E tests (both commercial & `ERGCTL_EDITION=oss`) |

## What It Does / Free Core vs. Pro

| Capability | Included In |
|---|---|
| `probe` — Discover BLE FTMS (5 machine classes), Concept2 PM5 BLE & USB HID, or 10-machine `--sim` | Free Core |
| `workout validate` — Schema & hardware capability check for `.json`, `.yaml`, `.erg`, `.mrc` | Free Core |
| `export` — Export recorded NDJSON logs to JSON, CSV, TCX, or binary ANT+ `.fit` (CRC-16) | Free Core |
| `--dry-run` safety previews across `control`, `workout run`, `tui`, and mutating MCP tools | Free Core |
| Unidirectional `stream` — Live telemetry/stroke/force-curve NDJSON monitoring | Free Core |
| `restore` — Baseline state stop, rollback replay & atomic snapshot cleanup | Free Core |
| Read-only & `dry_run: true` stdio JSON-RPC 2.0 MCP server (`ergctl mcp`, 16 tools, 4 `erg://` resources) | Free Core |
| Live `control` & `workout run` hardware execution (watts, speed, incline, resistance, bike aero sim) | Pro ($29 one-time) |
| Bidirectional AI-coaching `stream --bidirectional` with live stdin commands & `ERGCTL_WATCHDOG_MS` | Pro ($29 one-time) |
| Interactive raw-mode terminal `tui` & live mutating MCP control tools (`dry_run: false`) | Pro ($29 one-time) |

**Explicit Non-Goals & Honest Verification Disclosure:**
- **macOS Apple Silicon (`arm64`, macOS 14+) release binaries.** Zero proprietary vendor SDKs, kernel extensions, or DriverKit bridges.
- **Open specs only**: Bluetooth SIG FTMS (`0x1826` Data `0x2ACD/2ACE/2ACF/2AD1/2AD2`, Feature `0x2ACC`, Control Point `0x2AD9`, Status `0x2ADA`, Companion `0x180D/180F/180A`) and Concept2 PM5 open specifications (`CE060010/0020/0030/0080` + USB HID `0x17A4` CSAFE). Concept2 PM5 flywheel ergs expose `electronic_resistance: false` and `programmable_target_display: true`.
- **Headless macOS Bluetooth TCC note**: Unbundled terminal scans require macOS Bluetooth permission (`Privacy & Security > Bluetooth`) or `NSBluetoothAlwaysUsageDescription`; denied TCC exits deterministically (`exit 4`, `PERMISSION_DENIED`) instead of aborting (`--transport usb` and `--sim` do not require Bluetooth TCC).
- **Hardware testing scope**: All FTMS & PM5 wire codecs, BLE GATT characteristic routing (`0021`/`0022`/`0031`–`003D`/`0080`), USB HID CSAFE framing, ANT+ `.fit` binary CRC-16 encoding, `lstat`-guarded `0600` snapshots, loopback Polar licensing, real PTY `termios` raw-mode `tui` recovery, MCP `2024-11-05` stdio transport, `57` XCTests, and `208` E2E tests ran on Apple Silicon macOS. Physical BLE trainers and physical Concept2 PM5 monitors have **not** yet been attached to the build host — run `probe` and `--dry-run` first on live equipment.

## Install & Uninstall

### Homebrew (Recommended)
```bash
brew tap raydeoliveira/tap
brew install raydeoliveira/tap/ergctl
ergctl --version
```

### Release Tarball & SHA-256 Verification
```bash
tar -xzf ergctl-0.1.0-macos-arm64.tar.gz
shasum -a 256 -c SHA256SUMS.txt
install -m 755 ergctl-0.1.0-macos-arm64/ergctl /usr/local/bin/ergctl
ergctl --version
```

### Claude Desktop (One-Click `.mcpb`) & MCP Clients (Claude Code / Codex / Cursor)
Download `ergctl-0.1.0-macos-arm64.mcpb` from [GitHub Releases](https://github.com/raydeoliveira/ergctl/releases) and open it in Claude Desktop, or point any MCP client at Homebrew `ergctl`:

```json
{
  "mcpServers": {
    "ergctl": {
      "command": "ergctl",
      "args": ["mcp"],
      "env": {
        "ERGCTL_LICENSE_KEY": "<optional-polar-pro-key>"
      }
    }
  }
}
```

Install the companion AI agent skill (`SKILL.md`):
```bash
npx skills add raydeoliveira/ergctl
```

### Build From Source (Swift 6, macOS 14+)
```bash
# Commercial build (Free Core + Polar.sh Pro activation):
swift build -c release
swift test

# Open-Source Edition build (MIT seam, all features unlocked offline):
ERGCTL_EDITION=oss swift build -c release
ERGCTL_EDITION=oss swift test
```

### Uninstall
```bash
rm -f /usr/local/bin/ergctl
rm -rf ~/.config/ergctl
```

## Quick Start

### 1. Discover Machines & Inspect Capabilities (`probe`)
```bash
ergctl probe --sim --json
```
Real excerpt from Apple Silicon simulator output (`10` simulated devices across FTMS + PM5 BLE/USB):
```json
{"id":"sim-ftms-bike-1","machine_type":"indoor_bike","name":"Sim Kickr FTMS Bike","protocols":["ftms"],"transport":"sim"}
```

### 2. Validate & Run Workouts (`json`, `yaml`, `.erg`, `.mrc`)
```bash
ergctl workout validate examples/workout_sweet_spot.json --json
ergctl workout run examples/workout_rower.yaml --sim --device sim-pm5-ble-v2-row-1 --out row.ndjson --yes --json
```

### 3. Live Bidirectional AI-Coaching Loop & MCP Server
```bash
# Dry-run safety preview (Free, 0 hardware writes):
ergctl control --sim --device sim-ftms-bike-1 --watts 210 --dry-run --yes --json

# Live bidirectional AI coaching loop with 4s safety watchdog:
python3 examples/ai_coach_loop.py --bin "$(command -v ergctl)" --ticks 8 --watts 210

# Interactive terminal dashboard (real TTY required, Free/Pro):
ergctl tui --sim

# Export session to binary ANT+ .fit (validates 14B header + trailing CRC-16):
ergctl export row.ndjson --format fit --out workout.fit --json

# Stop hardware & roll back snapshots cleanly:
ergctl restore --sim --yes --json
```

## Safety, Watchdog & Exit Codes

Every mutating control path enforces: capability validation -> `lstat`-verified `0600` baseline snapshots -> `--dry-run` zero-write inspection -> `SafetyLimits` clamps (`--max-power`, `--max-speed`) -> `ERGCTL_WATCHDOG_MS` AI heartbeat auto-revert -> clean `SIGINT`/`SIGTERM` hardware stop (`exit 130`).

| Code | Meaning |
|---|---|
| `0` | Success (`"ok": true`) |
| `1` | Runtime error, decode/encode error, or watchdog/interrupt rollback |
| `2` | Invalid CLI syntax, out-of-range target, unsupported capability, or non-TTY `tui` |
| `3` | No matching FTMS/PM5 hardware connected |
| `4` | macOS Bluetooth TCC / USB HID permission denied or symlink output path rejected |
| `5` | Pro license missing/invalid/expired (omitted in `ERGCTL_EDITION=oss`) |
| `130` | Interrupted by `SIGINT`/`SIGTERM` after clean hardware stop |

## License & Support

- Commercial binary distribution is licensed under [LICENSE](LICENSE) (Free Core + `$29` one-time Perpetual Pro license via [Polar.sh](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT), up to 3 personal Macs, 14-day offline cache grace, zero telemetry).
- Security policy: [SECURITY.md](SECURITY.md) · Changelog: [CHANGELOG.md](CHANGELOG.md) · AI Agent Guide: [SKILL.md](SKILL.md) · MCP Manifest: [server.json](server.json).
