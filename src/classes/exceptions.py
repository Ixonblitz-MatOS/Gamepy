from . import ExceptionBase
class usedException:
    def __init__(self):
        self.world=ExceptionBase.WorldException
    def raiseWorld(self,message:str):
        raise self.world(message)
global exc
exc=usedException()