# Release Plan

## v0.1.0

- [x] Preserve the working BLE advertising behavior from the prototype
- [x] Create reusable `package.yaml`
- [x] Move local secrets, Wi-Fi, API, and OTA into user-owned YAML
- [x] Add editable `XGIMI Projector Key` text entity
- [x] Add key parsing validation before advertising
- [x] Add local and GitHub import examples
- [x] Add README setup notes
- [x] Add `.gitignore`, `LICENSE`, and `secrets.yaml.example`
- [ ] Validate with ESPHome compile
- [ ] Publish repository to GitHub
- [ ] Create GitHub release `v0.1.0`

## Release Notes Draft

Initial ESPHome package for ESP32 devices that act as Bluetooth proxies and advertise XGIMI wake manufacturer data.

Users provide Wi-Fi credentials, API encryption, OTA password, and their projector key in a local ESPHome YAML. The projector key can also be edited later from Home Assistant through the package's text entity.
