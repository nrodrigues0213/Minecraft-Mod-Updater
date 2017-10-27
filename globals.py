import platform
import os
import sys


INSTALL_DIRECTORY = ""

# CLIENT_VERSION_FILE contains the version of the latest mod files.
# This value can be changed to whatever you wish.
# This is checked against CLIENT_VERSION
CLIENT_VERSION_FILE = "clientversion.txt"

# CONSOLE_VERSION_FILE contains the version of the latest client executable.
# This value can be changed to whatever you wish.
# This console executable is created using pyinstaller.
CONSOLE_VERSION_FILE = "client_console_ver.txt"

# These are the URLs to your download locations.
CLIENT_DOWNLOAD_URL = "ENTER URL TO ALL OF YOUR MOD FILE DOWNLOADS"
CONSOLE_DOWNLOAD_URL = "ENTER URL TO ALL OF YOUR CONSOLE FILE DOWNLOADS"

CONSOLE_VERSION = "2.0.0"
CLIENT_VERSION = "0.0.0"
ONLINE_CLIENT_VERSION = "0.0.0"

OPERATING_SYSTEM = platform.system()

# determine location of executable depending on if it's a script or frozen exe
if getattr(sys, "frozen", False):
    APPLICATION_PATH = os.path.dirname(sys.executable) + "/"
else:
    APPLICATION_PATH = os.path.dirname(__file__) + "/"

# Dictionary containing the names of your mod's folder structure.
FOLDER_NAME = {
    0: "bin",
    1: "config",
    2: "mods"
}

MAIN_EXECUTABLE = {
    "Windows": "main.exe",
    "Linux": "main",
    "Darwin": "main"
}

BACKUP_EXECUTABLE = {
    "Windows": "main-backup.exe",
    "Linux": "main-backup",
    "Darwin": "main-backup"
}
