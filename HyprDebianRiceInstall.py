#!/usr/bin/env python3

# HyprDebianRice Install
# This script checks if you are using an apt-based paketmanager and
# if necessary, it will configure your sources.list. It will install
# Hyprland and some other packages. The packages are listed in Hypr-
# DebianRicePackages.

import subprocess
import shutil
import sys
from pathlib import Path

# 1. Debian and version check
os_release = {}

for line in Path("/etc/os-release").read_text().splitlines():
    if "=" in line:
        key, value = line.split("=", 1)
        os_release[key] = value.strip('"')

if os_release.get("ID") != "debian":
    print("Unsupported distribution")
    sys.exit(1)

version = os_release.get("VERSION_ID")

if version == "13":
    print("Debian 13 detected")
    sources = """Types: deb deb-src
URIs: https://deb.debian.org/debian
Suites: trixie-backports
Components: main
Enabled: yes
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
"""  
    try:
        subprocess.run(
            ["sudo", "tee", "/etc/apt/sources.list.d/debian-backports.sources"],
            input=sources,
            text=True,
            stdout=subprocess.DEVNULL,
            check=True
        )

        subprocess.run(
            ["sudo", "apt", "update"],
            check=True
        )

        subprocess.run(
            ["sudo", "apt", "install", "-t", "trixie-backports", "hyprland"],
            check=True
        )

    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen eines Befehls: {e}")
        sys.exit(1)

else:
    print(f"Unsupported Debian version: {version}")
    sys.exit(1)



