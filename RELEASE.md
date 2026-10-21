# Release Plan

## v0.1.1

- Restore wake advertising on ESPHome 2026.9 and later by configuring the BLE
  server with the idle manufacturer bytes `[0x46, 0x00]`.
- Preserve the wake payload, key handling, repeat count, and timing.
- Add ESP32 and ESP32-S3 configuration/code-generation checks on ESPHome
  2026.8.2, 2026.9.0, and 2026.10.0, plus full firmware builds on 2026.10.0.
- Verify live ESP32 (`esp32dev`) OTA installation through Home Assistant's
  ESPHome 2026.9.1 builder: the wake button brought independent Android TV
  remote/player entities online in approximately six seconds, with no errors
  in the bounded device-log capture.
- ESP32-S3 hardware confirmation on 2026.10.0 remains pending from the reporter.

Upgrade the GitHub package reference to `@v0.1.1`, then recompile and upload.
See [PR #2](https://github.com/bchevreau/esp32-bluetooth-proxy-xgimi-wake/pull/2)
and [issue #1](https://github.com/bchevreau/esp32-bluetooth-proxy-xgimi-wake/issues/1).

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
