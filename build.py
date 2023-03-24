#!/usr/bin/env python3

__author__ = "Akash9773312 @ keybase.io/akash9773312"

import PyInstaller.__main__ as pyinstaller


pyinstaller.run(("packet_sniffer/core.py", "--onefile"))