#!/usr/bin/python3

import os

from imports.shell import shell

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
def setup(folder_path) -> None:
    if os.path.exists(folder_path + "/DataBase"):
        pass
    else:
        os.mkdir(folder_path + "/DataBase")

    if os.path.exists(folder_path + "/DumpFolder"):
        pass
    else:
        os.mkdir(folder_path + "/DumpFolder")

    banner()

def main () -> None:
    main_folder_path = "~/RE_Engine"
    
    setup(main_folder_path)
    shell()
    
    
if __name__ == "__main__":
    main()
