## Minecraft Mod Updater
* Requires Python 3.6, Requests 2.18.4
* Distribute it with PyInstaller 3.3

Keep your private Minecraft mods up-to-date with your less technically gifted friends. 

Sharing your personal mod with friends can be challenging when they lack the computer knowledge to correctly install the files. This python script will take care of the process for them. 

# Features
- This script can automatically update itself so your users only need to install it once. Fix updater bugs and expand the feature set with ease.
- This script will download compressed (.zip) files from an online server, and will extract the contents into the user's minecraft directory.
- This script has been successfully tested on Microsoft Windows 10, Mac OS Sierra, and Linux (Ubuntu and Arch Linux distributions).

# Building executables with PyInstaller
Running 'pyinstaller -F main.py -n minecraft_updater' will create an executable file in a new 'dist' folder. This file will only work on the operating system that you built it on. That means that you must build the scripts on each operating system that you wish to support.

