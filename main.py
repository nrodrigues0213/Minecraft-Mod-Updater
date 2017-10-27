import os
import sys
import subprocess
import validator
import filehandler
import debug
import globals


def main():
    # Clear the terminal depending on OS.
    if globals.OPERATING_SYSTEM == "Darwin" or globals.OPERATING_SYSTEM == "Linux":
        os.system("clear")
    if globals.OPERATING_SYSTEM == "Windows":
        os.system("cls")
        
    debug.info("Welcome to the Banana Kingdom server updater V" + globals.CONSOLE_VERSION + "!")

    try:
        debug.info("Checking Internet connection..")
        if validator.check_internet():
            debug.success("Connected to the Internet!")
        else:
            debug.error("Failed Internet connection test.")
            debug.error("Terminating client launch.")
            debug.terminate()

        # If the updater has an update, it'll attempt to update itself.
        if validator.check_console_updates():
            update_executable = {
                "Windows": "update.exe",
                "Linux": "update",
                "Darwin": "update"
            }
            input("Press enter to install the new updates.")

            executable_path = os.path.join(globals.APPLICATION_PATH, update_executable[globals.OPERATING_SYSTEM])
            os.system(executable_path)
            sys.exit()

        # Delete backup of original executable, if the update was successful.
        if os.path.exists(globals.BACKUP_EXECUTABLE[globals.OPERATING_SYSTEM]):
            os.remove(globals.BACKUP_EXECUTABLE[globals.OPERATING_SYSTEM])

        debug.info("Would you like to check for updates?")
        install_confirm = input("Enter 'y' for yes or 'n' for no.")
        if not install_confirm == "y":
            sys.exit()

        if validator.check_directory():
            debug.success("Found your Minecraft installation in " + globals.INSTALL_DIRECTORY)
        else:
            debug.error("Failed to find Minecraft installation folder.")
            debug.error("Ending the update process.")
            debug.terminate()

        if not validator.check_version():
            debug.error("Failed to check your client version.")
            debug.error("Ending the update process.")
            debug.terminate()

        if filehandler.download_client():
            debug.success("Successfully downloaded client files!")
        else:
            debug.error("Failed to download client files.")
            debug.error("Ending the update process.")
            debug.terminate()

        filehandler.delete_folders()

        # Verify that the files were decompressed correctly.
        if filehandler.install_files():
            debug.success("Update Complete! Welcome to Banana Kingdom V"+globals.ONLINE_CLIENT_VERSION)
        else:
            debug.error("Failed to install required client files.")

    except OSError as e:
        debug.error("There was an error while running this program:")
        print(e)
    debug.terminate()

main()
