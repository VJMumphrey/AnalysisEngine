"""
Runs and handles the db used by the engine
"""

DEFAULT_PATH = "~/Database"

class db ():
    def __init__(self, session=1, path = DEFAULT_PATH) -> None:
        self.session = session
        self.path = path    

    def store(self, name="", signature="") -> None:


