# Changelog

All notable changes to `ergctl` are documented in this file.

## [0.2.0] - 2026-11-24

### Added & Improved
- **Generous Free Core Expansion (No License Required)**: Interactive raw-mode ANSI dashboard (`ergctl tui`), manual single-target live control (`ergctl control --watts`, `--speed`, `--incline`, `--resistance`, `--pause`, `--resume`, `--stop`, `--reset`), and MCP session `erg_export_session` (JSON, CSV, TCX, binary `.fit`) are now completely free in commercial builds so every trainer/PM5 owner can test real hardware and record/export workouts out of the box.
- **Focused `$29` Pro Tier**: Automated structured `workout run`, bidirectional AI-coaching loop (`stream --bidirectional`), aerodynamic bike simulation (`--grade`/`--wind-speed`/`--crr`/`--cw`), wheel/HR/spin-down/targeted-goal controls, and live MCP control tools require Pro (`$29` perpetual, 3 Macs), with direct checkout guidance embedded in CLI/MCP `LICENSE_INVALID` hints.
- **Hardware Compatibility Reporting Funnel**: Added GitHub issue template (`.github/ISSUE_TEMPLATE/hardware-report.md`) and compatible open-spec hardware matrix covering Wahoo KICKR, Tacx NEO/Flux, Concept2 RowErg/SkiErg/BikeErg PM5, Schwinn IC4/Bowflex/Stages FTMS, treadmills, and cross trainers.

## [0.1.0] - 2026-11-24

### Added
- **Bluetooth SIG FTMS v1.0 Codecs**: Indoor Bike (`0x2AD2`), Rower (`0x2AD1`), Treadmill (`0x2ACD`), Cross Trainer (`0x2ACE`), Step Climber (`0x2ACF`), Feature (`0x2ACC`), Training Status (`0x2AD3`), Supported Ranges (`0x2AD4..0x2AD8`), Control Point (`0x2AD9`), Machine Status (`0x2ADA`), and Companion GATT (`0x180D`, `0x180F`, `0x180A`).
- **Concept2 PM5 Open Spec Codecs**: BLE GATT `CE060010/0020/0030/0080` (`0031..003C`, `003D` Force Curve w/ legacy 18B/19B support, `HR=255 -> nil`, ATT MTU fragmentation) and USB HID CSAFE (`VID 0x17A4`, Report IDs `0x01/0x04/0x02`, `0xF3` byte stuffing).
- **Live macOS Adapters & Simulator**: `CoreBluetoothErgAdapter` (with TCC pre-check), `IOKitCSAFEAdapter`, and 10-device wire-codec `ProtocolSimulator`.
- **Workout Engine & Multi-Format Export**: Parser for JSON, YAML, `.erg`, and `.mrc` structured workouts plus `json`, `csv`, `tcx`, and binary `.fit` (with CRC-16) session export.
- **Safety, Live AI Stream & MCP Server**: `lstat`-guarded atomic snapshots, `ERGCTL_WATCHDOG_MS` baseline auto-revert, bidirectional NDJSON stream, interactive ANSI TUI (`termios`), and stdio JSON-RPC 2.0 MCP server (`2024-11-05`, 16 tools, 4 `erg://` resources).
- **Dual Edition Build**: Commercial Polar.sh licensing with 14-day offline grace and clean `-DOSS_EDITION` (`ERGCTL_EDITION=oss`) MIT compile seam.
