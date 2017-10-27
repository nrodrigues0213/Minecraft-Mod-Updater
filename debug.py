import sys


def info(output_text):
    print("[INFO] " + output_text)


def error(output_text):
    print("[ERROR] " + output_text)


def success(output_text):
    print("[SUCCESS] " + output_text)


def terminate():
    input("Press enter to continue..")
    sys.exit()