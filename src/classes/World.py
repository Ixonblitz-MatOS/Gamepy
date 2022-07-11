from typing import Tuple as t
from Character import Character
from Camera import Camera
from exceptions import exc
class World:
    def __init__(self,dimension:int,size:t[float],player:Character=None,mainCamera:Camera=None,Infinite:bool=False):
        self.infinite=Infinite
        if dimension >3: exc.raiseWorld("Dimension must be 3 or 2")

        else:self.dimension = dimension
        if(len(size)>3 or len(size)!=dimension):exc.raiseWorld("Size must match dimension and be withing 2 or 3")
        else: self.size=size
        self.origin=(0,0,0)
        self.showing=False
        self.objects=dict()
        self.player=player
        self.mainCamera=mainCamera
        self.CurrentSettings=dict()
    def addObj(self,obj):
        self.objects[obj.name]=obj
        self.CurrentSettings[obj.name]={}
    def showObjects(self):
        return self.objects
    def createWorld(self):
        self.showing=True

    def objUpdate(self,name:str,change:dict):
        if name not in self.objects:exc.raiseObj("Object Name could not be found")
        finalWord=""
        for i in change.keys():
            finalWord=i
            break
        if finalWord.__contains__("active"):
            self.CurrentSettings[name]["active"]=bool(change["active"])
            return
        elif finalWord.__contains__("full"):
            secondDict=change
            secondDict.pop(0)
            for i in secondDict.keys():
                self.CurrentSettings[name][i]=secondDict[i]
                #puts all settings under the name using key which is setting and gets that by indexing settings of dict
            del secondDict
            return
        elif finalWord.__contains__("pos"):
            second=change.pop(0)
            lst=list()
            for i in second:
                    lst.append(second[i])
            finalPos=tuple(lst)
            self.CurrentSettings[name]["pos"]=finalPos