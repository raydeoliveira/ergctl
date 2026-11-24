# Ergctl

> **Product Hub:** [raymonddeoliveira.com/software#ergctl](https://www.raymonddeoliveira.com/software#ergctl) · **Buy Ergctl Pro ($29):** [Polar Checkout](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT) · **Releases & Checksums:** [GitHub Releases](https://github.com/raydeoliveira/ergctl/releases) · **Verified MCP:** [Glama](https://glama.ai/mcp/servers/raydeoliveira/ergctl) · **Official MCP Registry:** [io.github.raydeoliveira/ergctl](https://registry.modelcontextprotocol.io/v0.1/servers?search=raydeoliveira/ergctl) · **Free Core:** `brew tap raydeoliveira/tap && brew install ergctl`

Zero-dependency macOS CLI, **free** interactive terminal dashboard (`tui`), **free** manual live control, structured workout engine, ANT+ `.fit` exporter, and live `--json` / MCP AI-coaching controller for **Bluetooth SIG FTMS v1.0 (`0x1826`)** and **Concept2 PM5 (`CE06xxxx` BLE GATT + `VID 0x17A4` USB HID CSAFE)** fitness ergometers.

Replaces **$20–$44/mo** closed trainer and indoor rowing subscriptions with one native **~1.9 MB** Apple Silicon binary — 100% open specs, zero proprietary SDKs, zero reverse-engineering risk, binary `.fit` export (CRC-16), and a live bidirectional AI-coaching loop.

## Try Free in 10 Seconds (Zero Hardware Needed)

```bash
brew tap raydeoliveira/tap
brew install raydeoliveira/tap/ergctl

# Free Core: launch interactive TUI dashboard against the built-in 10-machine simulator
ergctl tui --sim

# Or probe & control your real FTMS trainer or Concept2 PM5 in Free Core:
ergctl probe --json
ergctl control --watts 200 --yes --json
```

## Measured Footprint

Measured on Apple Silicon (`arm64-apple-macos14.0`, Swift 6.4.2):

| Metric | Measured Value |
|---|---|
| Stripped binary (`arm64`) | `1,988,432 bytes` (`1.90 MiB`) |
| Compressed release tarball (`.tar.gz`) | `~753 KB` (`0.72 MiB`, binary + docs + MCP manifest) |
| Claude Desktop bundle (`.mcpb`) | `~757 KB` (`0.72 MiB`, signed binary + MCP manifest + docs) |
| External runtime dependencies | `0` (Swift stdlib, Foundation, CoreBluetooth, IOKit, Darwin) |
| `--version` latency (10 subprocess runs) | `7.77 ms` median (`7.29–9.11 ms`) |
| Automated verification | `57` XCTests + `208` Python E2E tests (both commercial & `ERGCTL_EDITION=oss`) |

## Generous Free Core vs. $29 Pro

| Capability | Included In |
|---|---|
| `probe` — Discover BLE FTMS (5 machine classes), Concept2 PM5 BLE & USB HID, or 10-machine `--sim` | **Free Core** |
| `tui` — Interactive raw-mode ANSI dashboard (live watts, sparklines, HR zones, `+/−/Space/p/r/q/Esc`) | **Free Core** |
| Manual `control` — Live `--watts`, `--speed`, `--incline`, `--resistance`, `--pause`, `--resume`, `--stop`, `--reset` | **Free Core** |
| `workout validate` — Schema & hardware capability check for `.json`, `.yaml`, `.erg`, `.mrc` | **Free Core** |
| `export` — Export NDJSON logs to JSON, CSV, TCX, or binary ANT+ `.fit` (CRC-16) via CLI or MCP | **Free Core** |
| Unidirectional `stream` (`--json`), `--dry-run` safety previews, `restore` rollback & dry-run MCP | **Free Core** |
| Automated `workout run` engine (`.json`, `.yaml`, `.erg`, `.mrc` hands-free step control) | [Pro ($29 one-time)](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT) |
| Bidirectional AI-coaching `stream --bidirectional` (live `stdin` target/cue commands + `ERGCTL_WATCHDOG_MS`) | [Pro ($29 one-time)](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT) |
| Aero bike sim (`--grade`/`--wind-speed`/`--crr`/`--cw`), spin-down, wheel/HR targets & live Pro MCP writes | [Pro ($29 one-time)](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT) |

## Open-Spec Compatible Hardware Matrix

Implemented strictly from published **Bluetooth SIG FTMS v1.0** (`0x1826`) and **Concept2 PM5 BLE/CSAFE** specifications:

| Category | Representative Equipment Using These Open Specs | Spec & Transport | Status |
|---|---|---|---|
| Smart Bike Trainers & Smart Bikes | Wahoo KICKR / CORE / SNAP / BIKE, Tacx NEO / Flux, Elite Direto / Suito, Stages SB20, Schwinn IC4 / Bowflex C6 | FTMS Indoor Bike (`0x2AD2` + `0x2AD9`) BLE | Open-spec implemented · [Submit hardware report](https://github.com/raydeoliveira/ergctl/issues/new?template=hardware-report.md) |
| Concept2 PM5 Ergs | Concept2 RowErg, SkiErg, BikeErg (PM5 firmware) | PM5 BLE (`CE06xxxx`) + USB HID (`0x17A4` CSAFE) | Open-spec implemented · [Submit hardware report](https://github.com/raydeoliveira/ergctl/issues/new?template=hardware-report.md) |
| FTMS Rowers, Treadmills & Steppers | WaterRower / FTMS Rowers (`0x2AD1`), FTMS Treadmills (`0x2ACD`), Cross Trainers (`0x2ACE`), Step Climbers (`0x2ACF`) | FTMS Data + `0x2AD9` Control Point BLE | Open-spec implemented · [Submit hardware report](https://github.com/raydeoliveira/ergctl/issues/new?template=hardware-report.md) |

**Explicit Non-Goals & Honest Verification Disclosure:**
- **macOS Apple Silicon (`arm64`, macOS 14+) release binaries.** Zero proprietary vendor SDKs, kernel extensions, or DriverKit bridges. Concept2 PM5 flywheel ergs expose `electronic_resistance: false` and `programmable_target_display: true`.
- **Headless macOS Bluetooth TCC note**: Unbundled terminal scans require macOS Bluetooth permission (`Privacy & Security > Bluetooth`) or `NSBluetoothAlwaysUsageDescription`; denied TCC exits deterministically (`exit 4`, `PERMISSION_DENIED`) instead of aborting (`--transport usb` and `--sim` do not require Bluetooth TCC).
- **Verification disclosure**: All FTMS & PM5 wire codecs, BLE GATT routing (`0021`/`0022`/`0031`–`003D`/`0080`), USB HID CSAFE framing, ANT+ `.fit` binary CRC-16 encoding, `lstat`-guarded `0600` snapshots, loopback Polar licensing, real PTY `termios` raw-mode `tui` recovery, MCP `2024-11-05` stdio transport, `57` XCTests, and `208` E2E tests ran on Apple Silicon macOS. Physical third-party BLE trainers and physical Concept2 PM5 monitors have **not** yet been attached to the build host — test your hardware free with `probe`, `tui`, and `--dry-run` first!

## Install & Uninstall

### Homebrew (Recommended)
```bash
brew tap raydeoliveira/tap
brew install raydeoliveira/tap/ergctl
ergctl --version
```

### Release Tarball & SHA-256 Verification
```bash
tar -xzf ergctl-0.2.0-macos-arm64.tar.gz
shasum -a 256 -c SHA256SUMS.txt
install -m 755 ergctl-0.2.0-macos-arm64/ergctl /usr/local/bin/ergctl
ergctl --version
```

### Claude Desktop (One-Click `.mcpb`) & MCP Clients (Claude Code / Codex / Cursor)
Download `ergctl-0.2.0-macos-arm64.mcpb` from [GitHub Releases](https://github.com/raydeoliveira/ergctl/releases) and open it in Claude Desktop, or configure Homebrew `ergctl` in any MCP client:

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

### 1. Discover Machines & Control Manually (Free Core)
```bash
ergctl probe --sim --json
ergctl control --sim --device sim-ftms-bike-1 --watts 200 --yes --json
ergctl tui --sim
```

### 2. Validate, Run Workouts & Export `.fit`
```bash
# Free Core validation & export:
ergctl workout validate examples/workout_sweet_spot.json --json
ergctl export session.ndjson --format fit --out workout.fit --json

# Pro automated interval execution:
ergctl workout run examples/workout_rower.yaml --sim --device sim-pm5-ble-v2-row-1 --out row.ndjson --yes --json
```

### 3. Live Bidirectional AI-Coaching Loop & Safety Rollback
```bash
# Pro live bidirectional AI coaching loop with 4s safety watchdog:
python3 examples/ai_coach_loop.py --bin "$(command -v ergctl)" --ticks 8 --watts 210

# Stop hardware & roll back snapshots cleanly (Free Core):
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
| `5` | Pro automation license required or invalid/expired (`ERGCTL_EDITION=oss` omits `5`) |
| `130` | Interrupted by `SIGINT`/`SIGTERM` after clean hardware stop |

## License & Support

- Commercial binary distribution is licensed under [LICENSE](LICENSE) (Generous Free Core + `$29` one-time Perpetual Pro license via [Polar.sh](https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT), up to 3 personal Macs, 14-day offline cache grace, zero telemetry).
- Hardware compatibility reports: [Open a Hardware Report](https://github.com/raydeoliveira/ergctl/issues/new?template=hardware-report.md).
- Security policy: [SECURITY.md](SECURITY.md) · Changelog: [CHANGELOG.md](CHANGELOG.md) · AI Agent Guide: [SKILL.md](SKILL.md) · MCP Manifest: [server.json](server.json).
