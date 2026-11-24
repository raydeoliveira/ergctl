# Polar.sh Product Listing — Ergctl Pro (macOS Apple Silicon)

> Use this copy on Polar.sh (`https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT`).
> Enable Polar's built-in **License Keys** benefit (prefix: `ERGC`, activation limit: `3` machines per buyer, expiration: never / perpetual).

---

## Product Title
**Ergctl Pro — FTMS & Concept2 PM5 CLI + MCP Server (macOS)**

## Price & Billing Model
- **$29 USD** — One-time purchase (Perpetual License, v0.x updates included, up to 3 personal Macs). Replaces `$20–$44/mo` closed trainer & indoor rowing app subscriptions.
- **Generous Free Core** included free in the single native binary (`probe`, interactive raw-mode `tui`, manual live `control` for `--watts`/`--speed`/`--incline`/`--resistance`, `workout validate`, JSON/CSV/TCX/FIT `export`, `--dry-run`, unidirectional `stream`, `restore`, and read/export/dry-run MCP).

## Tagline (1-sentence summary)
Own your Wahoo, Tacx, Schwinn FTMS trainer, treadmill, rower, or Concept2 PM5 training stack in one tiny native macOS CLI and MCP server — 100% open specs, free live TUI & manual control, zero monthly fees, structured `.erg`/`.mrc`/YAML/JSON workouts, binary `.fit` export, and a live bidirectional AI-coaching loop.

## What Is Included in Pro ($29 Perpetual)
- **Structured Workout Engine (`ergctl workout run`)**: Execute `.erg`, `.mrc`, YAML, and JSON interval plans hands-free on live FTMS or Concept2 PM5 hardware with capability pre-validation, monotonic NDJSON recording, and `Ctrl-C` / `restore` rollback.
- **Bidirectional AI-Coaching Stream (`ergctl stream --bidirectional`)**: Feed telemetry, stroke mechanics, and Concept2 PM5 force curves directly to Claude, Codex, or custom Python coaches, accept real-time power/pace/cue commands on `stdin`, and enforce `ERGCTL_WATCHDOG_MS` baseline auto-revert if your coach disconnects.
- **Aerodynamic Bike Simulation & Calibration Controls**: Live gradient, headwind, `crr`, and `cw` simulation (`--grade`, `--wind-speed`, `--crr`, `--cw`), wheel circumference, HR-target mode, spin-down, and Concept2 PM5 workout/cue programming.
- **Full Mutating AI-Agent MCP Server (`ergctl mcp`)**: Unlocks live `dry_run: false` writes across all 16 stdio MCP `2024-11-05` tools (`erg_*`).

## Free Core vs. Pro Comparison

| Feature | Free Core | Pro ($29 one-time) |
|---|---|---|
| `probe` (BLE FTMS, PM5 BLE/USB HID, 10-machine `--sim`) | Included | Included |
| Interactive terminal `tui` (live sparklines, HR zones, `+/−/Space/p/r/q`) | Included | Included |
| Manual live `control` (`--watts`, `--speed`, `--incline`, `--resistance`, `--stop`/`--pause`/`--resume`) | Included | Included |
| `workout validate` (`.json`, `.yaml`, `.erg`, `.mrc`) | Included | Included |
| `export` (JSON, CSV, TCX, binary ANT+ `.fit` w/ CRC-16, CLI & MCP) | Included | Included |
| `--dry-run` safety previews, unidirectional `stream` & `restore` | Included | Included |
| Read-only & `dry_run: true` MCP tools (`ergctl mcp`) | Included | Included |
| Automated structured `workout run` interval engine | — | Included |
| Bidirectional AI-coaching `stream --bidirectional` & `WATCHDOG_MS` | — | Included |
| Bike aero sim (`--grade`/`--wind-speed`/`--crr`/`--cw`) & live Pro MCP writes | — | Included |

## Requirements & Honest Limits
- **OS & Architecture**: macOS 14.0+ (Sonoma or newer) on Apple Silicon (`arm64`). Zero third-party runtime dependencies.
- **Permissions & TCC**: Uses Apple `CoreBluetooth` and `IOKit` HID. Headless BLE scanning requires macOS Bluetooth TCC grant for your terminal/client app; denials exit deterministically (`exit 4`) with remediation hints (or use `--transport usb` / `--sim`).
- **Verification Disclosure**: All FTMS & PM5 wire codecs, BLE routing (`0021`/`0022`/`0031`–`003D`/`0080`), USB HID CSAFE framing, ANT+ FIT binary CRC-16 encoding, `lstat` symlink-safe snapshots, loopback Polar.sh licensing, real PTY `termios` raw-mode TUI, MCP `2024-11-05` stdio transport, 57 XCTests, and 208 E2E tests ran on Apple Silicon macOS. Physical third-party BLE FTMS trainers and physical Concept2 PM5 units were not attached to the build host during CI; test your hardware with the Free Core (`probe`, `tui`, manual `control`, `--dry-run`) first.

---

## Published Storefront & Directory Links
- **Checkout Link ($29 one-time):** https://buy.polar.sh/polar_cl_yZX7OxANm5KpsXGmC233dm9mMCtARhSPMuFjw0XfvhT
- **Checkout Link ID:** `b6af74a3-f45f-470f-a0cd-8e1f68c5bbe0`
- **Polar Product ID:** `05c0a93a-37c2-4665-a941-7a75d679d9fd`
- **Polar Benefit — License Keys (`ERGC`, `6aa47111-7587-44b8-9bba-a235f6a2c625`):** max `3` activations, perpetual (no expiration)
- **Polar Benefit — File Downloads (`0f379850-fcfe-4e51-9968-dda0aad35405`):** `ergctl-0.2.0-macos-arm64.tar.gz`, `ergctl-0.2.0-macos-arm64.mcpb`, `SHA256SUMS.txt`
- **Glama Verified MCP Listing:** https://glama.ai/mcp/servers/raydeoliveira/ergctl
- **Official MCP Registry:** https://registry.modelcontextprotocol.io/v0.1/servers?search=raydeoliveira/ergctl
