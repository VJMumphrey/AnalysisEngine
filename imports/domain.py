
class Domain ():

    def __init__(self, domain="") -> None:
        self.domain = domain
    
    # -- acessors and mutators -- 

    @property
    def setDomain(self) -> str:
        return self._domain

    @setDomain.setter
    def getDomain(self) -> None:
        self._domain = self.domain

    # -- methods -- 

    
