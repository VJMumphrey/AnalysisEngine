import os
import time
import json

class File ():
    
    def __init__(self, name="", path="", packedStatus=False, signature="") -> None:
        self.name = name
        self.path = path
        self.packedStatus = packedStatus
        self.signature = signature

    # -- acessors and mutators --

    @property
    def setName(self) -> str:
        return self._name

    @property
    def setPath(self) -> str:
        return self._path

    @property
    def setPackedStatus(self) -> bool:
        return self._packedStatus

    @property
    def setSignature(self) -> str:
        return self._signature

    @setName.setter
    def getName(self) -> None:
        self._name = self.name

    @setPath.setter
    def getPath(self) -> None:
        self._path = self.path

    @setPackedStatus.setter
    def getPackedStatus(self) -> None:
        self._packedStatus = self.packedStatus

    @setSignature.setter
    def getSignature(self) -> None:
        self._signature = self.signature

    # -- methods -- 

    def createFolder(self) -> None:
        # creates a folder with the name and date of analysis of the filename

        path = os.path.join(".", self.name + time.localtime())
        os.mkdir(path)

    def neuterFile(self) -> None:
        # defangs the malware by adding a file exenstion to it
        os.rename(self.name, self.name + ".malw")

    def depositFile(self) -> None:
        pass

    def displayResults(self) -> None:
        # display the results of the json recived from vt
        pass

    def changePackedStatus(self) -> None:
        # change the packed attribute of a file

        if self.getPackedStatus == False:
            self.setPackedStatus(True)
    
