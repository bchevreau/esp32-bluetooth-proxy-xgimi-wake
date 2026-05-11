# ESP32 Bluetooth Proxy XGIMI Wake

ESPHome package for an ESP32 that works as a Bluetooth proxy and advertises the BLE manufacturer payload used to wake XGIMI projectors, including the XGIMI Horizon S Max.

The package keeps the XGIMI manufacturer/company ID fixed at `0x0046`. You provide your projector key, either from a local secret at first flash or later through the editable Home Assistant text entity.

## What This Includes

- Bluetooth proxy support
- Active BLE tracker
- BLE server advertising support
- A Home Assistant button named `XGIMI Projector Wakeup`
- An editable Home Assistant text entity named `XGIMI Projector Key`
- Validation for malformed hex keys before advertising

## Repository Layout

- `package.yaml` - reusable ESPHome package
- `esp32-bluetooth-proxy-xgimi-wake.yaml` - local development example
- `examples/xgimi-wake-proxy.yaml` - GitHub package import example
- `secrets.yaml.example` - local secrets template
- `RELEASE.md` - first release checklist
- `LICENSE` - MIT license

## Install From GitHub

Create a local ESPHome YAML file like this:

```yaml
substitutions:
  name: xgimi-wake-proxy
  friendly_name: XGIMI Wake Proxy
  xgimi_projector_key: !secret xgimi_projector_key

packages:
  xgimi_wake: github://bchevreau/esp32-bluetooth-proxy-xgimi-wake/package.yaml@v0.1.0

api:
  encryption:
    key: !secret api_key

ota:
  - platform: esphome
    password: !secret ota_password

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password
  power_save_mode: none
```

Then add the matching values to your local `secrets.yaml`:

```yaml
api_key: "YOUR_API_ENCRYPTION_KEY"
ota_password: "YOUR_OTA_PASSWORD"
wifi_ssid: "YOUR_WIFI_SSID"
wifi_password: "YOUR_WIFI_PASSWORD"
xgimi_projector_key: "5e eb cf 58 39 54 38 ff ff ff 30 43 52 4b 54 4d"
```

Compile and upload with ESPHome:

```bash
esphome run xgimi-wake-proxy.yaml
```

## Projector Key

The projector key is the manufacturer data value after the company ID. This package prepends the company ID bytes automatically:

```text
46 00 <your projector key bytes>
```

Example key formats accepted by the package:

```text
5eebcf58395438ffffff3043524b544d
5e eb cf 58 39 54 38 ff ff ff 30 43 52 4b 54 4d
5e:eb:cf:58:39:54:38:ff:ff:ff:30:43:52:4b:54:4d
```

After first upload, you can edit `XGIMI Projector Key` from Home Assistant. ESPHome stores the text value on the device, so changing it does not require a new firmware upload.

Because the text entity uses `restore_value`, `xgimi_projector_key` is mainly the first-boot seed value. Once the device has stored a key, update it from Home Assistant rather than expecting a changed secret to overwrite the restored value on every upload.

## Finding Your XGIMI Token

For token discovery instructions, see the excellent XGIMI integration by manymuch:

https://github.com/manymuch/Xgimi-4-Home-Assistant

That project documents the token retrieval process this package relies on.

## OTA And Git Packages

OTA does not update this repository or pull changes from GitHub by itself. OTA is only the upload mechanism for a firmware image ESPHome has already compiled.

When you run ESPHome from Home Assistant or the CLI, ESPHome reads your local YAML, fetches the Git package if needed, compiles one complete firmware image, and then uses `ota: platform: esphome` to upload that image to the ESP32.

To receive changes from this package repo, update the package ref in your local YAML or use a newer release tag, then compile and upload again.

## Notes

- Remote ESPHome packages cannot contain `!secret` lookups. Secrets belong in the local YAML that imports the package.
- The editable projector key is convenient, but it is visible to users who can access the ESPHome device in Home Assistant.
- `esp32_ble_server` is intentionally included because the wake action depends on active BLE advertising.
