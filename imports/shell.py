from imports.filehandle import File
from imports.domain import Domain
from imports.url import Url
from imports.unpacme import unpac
from imports.signature import gensignature
from imports.vtcontroller import *

"""
Controls the shell system that runs normal unix commands
When a command is inputed from the program then it executes it
"""

def changeKey(key) -> None:
    # change the key in vtlookup
    pass

def shell() -> None:

    # create default values
    userInput = ""
    file = File(name="", path="")

    # run till the user quits 
    while(userInput.lower() != "q" or "quit"):
        print("RE_Engine> ", end="")
        
        userInput = str(input())

        # take the user input and split it up for usage
        inputLs = userInput.split(" ")


        if (inputLs[0] == "scan file"):
            # lookup info about the file
            # if there is no info then it will scan file
            file = File(name="", path=inputLs[1])
            lookupFile(file)

        elif (inputLs[0] == "scan url"):
            # lookup the url
            url = Url(inputLs[1])
            lookupUrl(url.url)

        elif (inputLs[0] == "lookupD"):
            domain = Domain(domain=inputLs[1])
            lookupDomain(domain)

        elif (inputLs[0] == "changeKey"):
            changeKey(inputLs[1])

        # utilize unpacme to get the unpacked verison of the malware
        if (file.getPackedStatus == True):
           unpac(file) 
        
        # generate the signatures and store in the DataBase
        gensignature(file)
        store(file)

        # defang the malware and store it away
        file.neuterFile()
        file.createFolder()
