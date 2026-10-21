"""Check that the generated BLE server requests advertising, without real secrets."""

import argparse
from importlib.metadata import version
from pathlib import Path
import re
import subprocess
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compile", action="store_true", help="also compile both firmwares")
    args = parser.parse_args()
    tests = Path(__file__).resolve().parent
    esphome_version = version("esphome")
    release = tuple(int(part) for part in esphome_version.split(".")[:2])
    print(f"Validating with ESPHome {esphome_version}", flush=True)

    for board in ("esp32", "esp32-s3"):
        command = [sys.executable, "-m", "esphome", "compile", str(tests / f"{board}.yaml")]
        subprocess.run([*command, "--only-generate"], check=True)
        source = tests / ".esphome" / "build" / f"xgimi-test-{board}" / "src" / "main.cpp"
        generated = source.read_text(encoding="utf-8")

        # A configured manufacturer payload makes the server own an advertising
        # request. With the original empty server, 2026.9+ emits false here.
        if release >= (2026, 9):
            if not re.search(r"->set_advertising_required\(true\);", generated):
                raise AssertionError(f"{board}: BLE server does not request advertising")
        if not re.search(r"->set_manufacturer_data\(\{(?:0x46|70),\s*(?:0x00|0)\}\);", generated):
            raise AssertionError(f"{board}: missing idle XGIMI manufacturer payload")

        print(f"PASS: {board} advertising configuration", flush=True)
        if args.compile:
            subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
