
class Url():

    def __init__(self, url="") -> None:
        self.url = url

    # -- acessors and mutators --

    @property
    def setUrl(self):
        return self._url

    @setUrl.setter
    def getUrl(self):
        self._url = self.url

    # -- methods -- 
