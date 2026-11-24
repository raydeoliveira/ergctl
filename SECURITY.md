# Security Policy — Ergctl

## Reporting a Vulnerability
Report security or hardware-safety vulnerabilities privately via GitHub Security Advisories on `https://github.com/raydeoliveira/ergctl`.

## Security & Hardware Safety Model
- **Zero external dependencies**: Built exclusively on Swift standard library, `Foundation`, `CoreBluetooth`, `IOKit`, and `Darwin`.
- **Zero background telemetry**: Makes no background network calls. Outbound HTTPS runs only during explicit `ergctl license activate` / `deactivate` calls against Polar.sh in commercial builds.
- **Symlink & path-traversal protection**: Snapshot storage and session exporters validate keys/paths and check symlinks with `lstat` before reading or writing (`0600` file permissions for snapshots and cached license tokens).
- **Hardware safety & rollback**: Every mutating command supports `--dry-run`, clamps within capability bounds, enforces `SafetyLimits` and `ERGCTL_WATCHDOG_MS` timeout auto-revert, and stops hardware cleanly on `SIGINT`/`SIGTERM` or `restore`.
