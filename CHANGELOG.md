# Changelog

All notable changes to `ergctl` are documented in this file.

## [0.1.0] - 2026-11-24

### Added
- **Bluetooth SIG FTMS v1.0 Codecs**: Indoor Bike (`0x2AD2`), Rower (`0x2AD1`), Treadmill (`0x2ACD`), Cross Trainer (`0x2ACE`), Step Climber (`0x2ACF`), Feature (`0x2ACC`), Training Status (`0x2AD3`), Supported Ranges (`0x2AD4..0x2AD8`), Control Point (`0x2AD9`), Machine Status (`0x2ADA`), and Companion GATT (`0x180D`, `0x180F`, `0x180A`).
- **Concept2 PM5 Open Spec Codecs**: BLE GATT `CE060010/0020/0030/0080` (`0031..003C`, `003D` Force Curve w/ legacy 18B/19B support, `HR=255 -> nil`, ATT MTU fragmentation) and USB HID CSAFE (`VID 0x17A4`, Report IDs `0x01/0x04/0x02`, `0xF3` byte stuffing).
- **Live macOS Adapters & Simulator**: `CoreBluetoothErgAdapter` (with TCC pre-check), `IOKitCSAFEAdapter`, and 10-device wire-codec `ProtocolSimulator`.
- **Workout Engine & Multi-Format Export**: Parser for JSON, YAML, `.erg`, and `.mrc` structured workouts plus `json`, `csv`, `tcx`, and binary `.fit` (with CRC-16) session export.
- **Safety, Live AI Stream & MCP Server**: `lstat`-guarded atomic snapshots, `ERGCTL_WATCHDOG_MS` baseline auto-revert, bidirectional NDJSON stream, interactive ANSI TUI (`termios`), and stdio JSON-RPC 2.0 MCP server (`2024-11-05`, 16 tools, 4 `erg://` resources).
- **Dual Edition Build**: Commercial Polar.sh licensing with 14-day offline grace and clean `-DOSS_EDITION` (`ERGCTL_EDITION=oss`) MIT compile seam.
