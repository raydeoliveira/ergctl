# Polar.sh Product Listing — Ergctl Pro (macOS Apple Silicon)

> Use this copy directly when creating the Ergctl Pro product in your Polar.sh dashboard (`polar.sh`).
> Enable Polar's built-in **License Keys** benefit (prefix: `ERGC`, activation limit: `3` machines per buyer, expiration: never / perpetual).

---

## Product Title
**Ergctl Pro — Open FTMS & Concept2 PM5 Ergometer CLI, AI Coach Stream & MCP Server (macOS)**

## Price & Billing Model
- **$29 USD** — One-time purchase (Perpetual License, v0.x updates included, up to 3 personal Macs). Replaces `$20–$44/mo` closed trainer & indoor rowing app subscriptions.
- **Free Core Tier** included in the exact same single native binary (`probe`, `workout validate`, JSON/CSV/TCX/FIT `export`, `--dry-run`, unidirectional telemetry `stream`, `restore`, read-only/dry-run MCP).

## Tagline (1-sentence summary)
Own your indoor bike, rower, treadmill, SkiErg, and Concept2 PM5 training stack in one tiny native macOS CLI and MCP server — 100% open specs, zero monthly fees, structured `.erg`/`.mrc`/YAML/JSON workouts, binary `.fit` export, and a live AI-coaching control loop.

## What Is Included in Pro ($29 Perpetual)
- **Live Hardware Control (`ergctl control`)**: Safety-guarded ERG target watts, treadmill speed & incline grade, resistance level, wheel circumference, spin-down, and bike aerodynamic simulation (`wind_speed_mps`, `grade_percent`, `crr`, `cw`) over Bluetooth SIG FTMS (`0x1826`) and Concept2 PM5 BLE/USB CSAFE.
- **Structured Workout Execution (`ergctl workout run`)**: Run `.erg`, `.mrc`, YAML, and JSON interval plans on live ergometers with capability pre-validation, monotonic NDJSON recording, and `Ctrl-C` / `restore` rollback.
- **Bidirectional AI-Coaching Stream (`ergctl stream --bidirectional`)**: Feed telemetry + stroke/force-curve NDJSON frames directly to Claude, Codex, or custom Python coaches, accept live power/pace/cue commands on `stdin`, and enforce `ERGCTL_WATCHDOG_MS` baseline auto-revert if your coach disconnects.
- **Interactive Terminal Dashboard (`ergctl tui`) & Live MCP Server (`ergctl mcp`)**: Raw-mode ANSI sparklines, heart-rate zone bar, and live control keys (`+/−/Space/p/r/q/Esc`), plus full mutating control across all 16 stdio MCP `2024-11-05` tools (`erg_*`).

## Free Core vs. Pro Comparison

| Feature | Free Core | Pro ($29 one-time) |
|---|---|---|
| `probe` (BLE FTMS, PM5 BLE/USB HID, 10-machine `--sim`) | Included | Included |
| `workout validate` (`.json`, `.yaml`, `.erg`, `.mrc`) | Included | Included |
| `export` (JSON, CSV, TCX, binary ANT+ `.fit` w/ CRC-16) | Included | Included |
| `--dry-run` safety previews (`control`, `workout run`, `mcp`) | Included | Included |
| Unidirectional `stream` live NDJSON monitoring | Included | Included |
| `restore` baseline stop & snapshot cleanup | Included | Included |
| Read-only & `dry_run: true` MCP tools (`ergctl mcp`) | Included | Included |
| Live `control` & `workout run` hardware execution | — | Included |
| Bidirectional AI-coaching `stream --bidirectional` | — | Included |
| Interactive terminal `tui` & live Pro MCP write tools | — | Included |

## Requirements & Honest Limits
- **OS & Architecture**: macOS 14.0+ (Sonoma or newer) on Apple Silicon (`arm64`). Zero third-party runtime dependencies.
- **Permissions & TCC**: Uses Apple `CoreBluetooth` and `IOKit` HID. Headless BLE scanning requires macOS Bluetooth TCC grant for your terminal/client app; denials exit deterministically (`exit 4`) with remediation hints (or use `--transport usb` / `--sim`).
- **Verification Disclosure**: All FTMS & PM5 wire codecs, BLE routing (`0021`/`0022`/`0031`–`003D`/`0080`), USB HID CSAFE framing, ANT+ FIT binary CRC-16 encoding, `lstat` symlink-safe snapshots, loopback Polar.sh licensing, real PTY `termios` raw-mode TUI, MCP `2024-11-05` stdio transport, 57 XCTests, and 208 E2E tests ran on Apple Silicon macOS. Physical third-party BLE FTMS machines and physical Concept2 PM5 units were not attached to the build host during CI; validate your unit with `probe` and `--dry-run` first.

---

## Seller Launch Checklist (Polar.sh Dashboard)
1. Create Product at `https://polar.sh/dashboard` (`Raymond de Oliveira` org `e00cbb5a-4317-4193-950c-10f7ec4dcd90`) -> **One-time purchase -> $29 USD**.
2. Add Benefit -> **License Keys**: prefix `ERGC`, limit activations = `3`, expiration = `Never`.
3. Add Benefit -> **File Downloads**: upload from `projects/ergctl/dist/`:
   - `ergctl-0.1.0-macos-arm64.tar.gz`
   - `ergctl-0.1.0-macos-arm64.mcpb`
   - `SHA256SUMS.txt`
4. Copy the generated `buy.polar.sh/polar_cl_...` checkout URL into `README.md`, `raydeoliveira/raydeoliveira`, and `raymonddeoliveira.com/software.html`.
