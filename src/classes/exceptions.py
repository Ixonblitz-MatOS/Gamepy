from . import ExceptionBase
class usedException:
    def __init__(self):
        self.world=ExceptionBase.WorldException
        self.camera=ExceptionBase.CameraException
        self.character=ExceptionBase.CharacterException
        self.obj=ExceptionBase.ObjectException
    def raiseWorld(self,message:str):
        raise self.world(message)
    def raiseCamera(self,message:str):
        raise self.camera(message)
    def raiseCharacter(self,message:str):
        raise self.character(message)
    def raiseObj(self,message:str):
        raise self.obj(message)
global exc
exc=usedException()