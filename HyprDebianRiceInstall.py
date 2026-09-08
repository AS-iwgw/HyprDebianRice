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
elif version == "14":
    print("Debian 14 detected")
else:
    print(f"Unsupported Debian version: {version}")
    sys.exit(1)
