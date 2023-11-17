#!/usr/bin/python3

import os
from imports.shell import shell

MAIN_FOLDER_PATH = "~/RE_ENGINE"
DB_PATH = MAIN_FOLDER_PATH + "/DATABASE"
DMP_PATH = MAIN_FOLDER_PATH + "/DUMPFOLDER"

# displays the banner on startup
# (temp)
def banner() -> None:
    termSize = os.get_terminal_size()
    column = termSize[0]
    lines = termSize[1]
    print("/" * column) 

    print("RE_ENGINE")

    print("'\'" * column)


# run everytime
# check for complete setup
def setup() -> None:
    if os.path.exists(MAIN_FOLDER_PATH):
        pass
    else:
        os.mkdir(MAIN_FOLDER_PATH)

    if os.path.exists(DB_PATH):
        pass
    else:
        os.mkdir(DB_PATH)

    if os.path.exists(DMP_PATH):
        pass
    else:
        os.mkdir(DMP_PATH)

    banner()

def main ():
    setup()
    shell()

if __name__ == "__main__":
   main()
