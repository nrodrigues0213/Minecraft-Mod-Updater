import debug
import globals
import os
import shutil
import queue
import requests
import zipfile
from urllib.error import URLError


# Downloads a file at url and names it filename
def download(url, filename):
    try:
        debug.info("Downloading files from "+url)
        web_request = requests.get(url)
        with open(filename, "wb") as file:
            file.write(web_request.content)
        return os.path.isfile(filename)
    except (IOError, URLError) as e:
        debug.error("There was an error while downloading the file.")
        print(e)
        return False


# Downloads the client zip file according to values in the globals file
def download_client():
    try:
        client_file = "clientfiles("+globals.ONLINE_CLIENT_VERSION+").zip"
        if os.path.isfile(globals.INSTALL_DIRECTORY + client_file):
            debug.info("Found client files within " + globals.INSTALL_DIRECTORY + client_file)
            debug.info("Deleting existing client files..")
            os.remove(globals.INSTALL_DIRECTORY + client_file)

        new_client_file = "clientfiles("+globals.ONLINE_CLIENT_VERSION+").zip"
        return download(globals.CLIENT_DOWNLOAD_URL + client_file, globals.INSTALL_DIRECTORY + new_client_file)
    except (IOError, OSError) as e:
        debug.error("There was an error while installing the latest client files.")
        print(e)
        return False


# Deletes all mod folders if they exist
def delete_folders():
    try:
        for i in range(0, len(globals.FOLDER_NAME)):
            debug.info("Looking for "+globals.FOLDER_NAME[i]+"...")
            if os.path.isdir(os.path.join(globals.INSTALL_DIRECTORY, globals.FOLDER_NAME[i])):
                debug.info("Clearing "+ globals.INSTALL_DIRECTORY + globals.FOLDER_NAME[i] +".")
                shutil.rmtree(globals.INSTALL_DIRECTORY + globals.FOLDER_NAME[i])
            else:
                debug.info(globals.FOLDER_NAME[i] + " folder not found. This is fine.")
    except (OSError, IOError) as e:
        debug.error("The program encountered an error while trying to empty client folders.")
        print(e)
        debug.terminate()


def install_files():
    try:
        new_client_file = "clientfiles(" + globals.ONLINE_CLIENT_VERSION + ").zip"
        client_zip = zipfile.ZipFile(globals.INSTALL_DIRECTORY + new_client_file, "r")
        client_zip.extractall(globals.INSTALL_DIRECTORY)
        client_zip.close()
        for i in range(0, len(globals.FOLDER_NAME)):
            debug.info("Verifying the installation of "+globals.FOLDER_NAME[i]+"...")
            if os.path.isdir(globals.INSTALL_DIRECTORY + globals.FOLDER_NAME[i]):
                debug.success("Installation found: "+globals.FOLDER_NAME[i]+".")
            else:
                debug.info(globals.FOLDER_NAME[i] + " could not be found!")
                return False
        return True
    except (OSError, IOError) as e:
        debug.error("Failed to install client files.")
        print(e)
        return False
