import socket
import getpass
import os
import shutil
import debug
import filehandler
import globals
from urllib.error import URLError


def check_internet():
    try:
        host_name = socket.gethostbyname("www.google.com")
        socket.create_connection((host_name, 80), 2)
        return True
    except OSError:
        pass
    return False


def check_console_updates():
    try:
        filehandler.download(globals.CONSOLE_DOWNLOAD_URL + globals.CONSOLE_VERSION_FILE,
                             globals.APPLICATION_PATH + globals.CONSOLE_VERSION_FILE)
        with open(globals.APPLICATION_PATH + globals.CONSOLE_VERSION_FILE) as console_file:
            online_console_version = console_file.read().replace("\n", "")
        if online_console_version == "":
            online_console_version = "0.0.0"

        os.remove(globals.APPLICATION_PATH + globals.CONSOLE_VERSION_FILE)
        if online_console_version == globals.CONSOLE_VERSION:
            return False
        else:
            debug.info("New updater version available!")
            debug.info("Version available: V" + online_console_version)
            return True
    except (IOError, URLError) as e:
        debug.error("There was an error while trying to receive version data.")
        print(e)
        debug.error("Terminating updater launch.")
        return False


def check_directory():
    debug.info("Looking for Minecraft installation folder..")

    if not globals.INSTALL_DIRECTORY == "":
        debug.info("Looking within "+globals.INSTALL_DIRECTORY)
        if not os.path.isdir(globals.INSTALL_DIRECTORY):
            globals.INSTALL_DIRECTORY = ""

    if globals.INSTALL_DIRECTORY == "":
        if globals.OPERATING_SYSTEM == "Windows":
            windows_mc_folder = os.path.join(os.getenv('APPDATA'), ".minecraft/")
            debug.info("Looking within your " + windows_mc_folder)
            if os.path.isdir(windows_mc_folder):
                globals.INSTALL_DIRECTORY = windows_mc_folder

        if globals.OPERATING_SYSTEM == "Linux":
            linux_mc_folder = os.path.join(os.path.expanduser("~"), ".minecraft/")
            debug.info("Looking within your " + linux_mc_folder + " folder.")
            if os.path.isdir(linux_mc_folder):
                globals.INSTALL_DIRECTORY = linux_mc_folder

        if globals.OPERATING_SYSTEM == "Darwin":
            mac_mc_folder = os.path.join(os.path.expanduser("~"), "Library/Application Support/minecraft/")
            debug.info("Looking within your " + mac_mc_folder + " folder.")
            if os.path.isdir(mac_mc_folder):
                globals.INSTALL_DIRECTORY = mac_mc_folder
    return not globals.INSTALL_DIRECTORY == ""


def check_version():
    try:
        if os.path.isfile(globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE):
            debug.info("Found client version file in "+globals.INSTALL_DIRECTORY)
            with open(globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE) as current_version_file:
                globals.CLIENT_VERSION = current_version_file.read().replace("\n", "")
            current_version_file.close()
            debug.info("Contents of client version file: "+globals.CLIENT_VERSION)

        filehandler.download(globals.CLIENT_DOWNLOAD_URL + globals.CLIENT_VERSION_FILE,
                             globals.CLIENT_VERSION_FILE)
        debug.info("Saved client version file to ./"+globals.CLIENT_VERSION_FILE)
        with open(globals.CLIENT_VERSION_FILE, "r") as online_version_file:
            globals.ONLINE_CLIENT_VERSION = online_version_file.read().replace("\n", "")

        debug.info("Current client version: "+globals.CLIENT_VERSION)
        debug.info("Latest client version: "+globals.ONLINE_CLIENT_VERSION)
        if globals.CLIENT_VERSION == globals.ONLINE_CLIENT_VERSION:
            debug.success("Your client is up to date!")
            os.remove(globals.CLIENT_VERSION_FILE)
            debug.terminate()

        if os.path.isfile(globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE):
            debug.info("Deleting old version data..")
            os.remove(globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE)

        debug.success("Deleted old version data!")
        debug.info("Installing new version data..")
        shutil.move(globals.CLIENT_VERSION_FILE, globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE)
        return os.path.isfile(globals.INSTALL_DIRECTORY + globals.CLIENT_VERSION_FILE)
    except (OSError, URLError) as e:
        debug.error("There was an error while checking the version of your client:")
        print(e)
        return False
