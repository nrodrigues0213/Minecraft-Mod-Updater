import os
import debug
import globals
import filehandler
from urllib.error import URLError


def update_console():
    debug.info("Saving current updater files..")
    try:
        os.rename(globals.APPLICATION_PATH + globals.MAIN_EXECUTABLE[globals.OPERATING_SYSTEM],
                  globals.APPLICATION_PATH + globals.BACKUP_EXECUTABLE[globals.OPERATING_SYSTEM])
        debug.success("Successfully saved updater files!")
        debug.info("Downloading new updater files.")

        debug.info("This may take a minute.")
        if filehandler.download(globals.CONSOLE_DOWNLOAD_URL + globals.OPERATING_SYSTEM + "/" + globals.MAIN_EXECUTABLE[globals.OPERATING_SYSTEM],
                                globals.APPLICATION_PATH + globals.MAIN_EXECUTABLE[globals.OPERATING_SYSTEM]):
            debug.success("Downloaded updater files.")
        else:
            debug.error("Failed to download new updater files.")
            debug.error("Ending the update process.")
            debug.terminate()

        if globals.OPERATING_SYSTEM == "Linux" or globals.OPERATING_SYSTEM == "Darwin":
            debug.info("Applying file permissions..")
            os.system("sudo chmod +x " + globals.APPLICATION_PATH + "main")

        debug.success("Update completed!")
        debug.terminate()
    except URLError as e:
        debug.error("Failed to download new updater files.")
        print(e)
        debug.info("Loading saved files.")
        os.rename(globals.APPLICATION_PATH + globals.BACKUP_EXECUTABLE, globals.APPLICATION_PATH + globals.MAIN_EXECUTABLE)
        debug.success("Loaded saved files!")
        debug.success("Ending update process.")
        debug.terminate()
    except OSError as e:
        debug.error("The updater encountered an error:")
        print(e)
        debug.error("Terminating update.")
        debug.terminate()

update_console()
