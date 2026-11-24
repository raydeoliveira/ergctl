---
name: Hardware Compatibility Report
about: Share a 30-second test report from a real FTMS trainer, treadmill, rower, or Concept2 PM5
title: "[Hardware] <Brand Model> — <BLE FTMS / PM5 BLE / PM5 USB>"
labels: hardware-report
---

Thanks for testing `ergctl` on real hardware! Free Core includes `probe`, `tui`, manual `control`, and `.fit` export with zero license required.

### Ergometer Details
- **Brand & Model**: (e.g., Wahoo KICKR v6, Tacx NEO 2T, Concept2 RowErg PM5, Schwinn IC4)
- **Connection**: BLE FTMS (`0x1826`) / Concept2 PM5 BLE (`CE06xxxx`) / Concept2 PM5 USB (`0x17A4`)
- **macOS & Chip**: (e.g., macOS 15.x, Apple M3 Pro)
- **`ergctl --version`**: (paste output)

### Check What Worked
- [ ] `ergctl probe --json` discovered the unit cleanly
- [ ] `ergctl tui` displayed live cadence/speed/power/pace/HR
- [ ] `ergctl control --watts <W>` / `--speed` / `--incline` / `--resistance --yes` updated the ergometer
- [ ] `ergctl export ... --format fit` produced a valid `.fit` file
- [ ] `ergctl restore --yes` stopped/restored cleanly

### `ergctl probe --json` Output (optional, redact serial if desired)
```json
```

### Notes / Any Unexpected Behavior
(Paste any `ERGCTL_*` errors, firmware details, or quirks.)
