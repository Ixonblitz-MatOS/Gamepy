from typing import Tuple as t

from exceptions import exc
class World:
    def __init__(self,dimension:int,size:t[float],character=):
        if dimension >3: exc.raiseWorld("Dimension must be 3 or 2")
        else:self.dimension = dimension
        if(len(size)>3 or len(size)!=dimension):exc.raiseWorld("Size must match dimension and be withing 2 or 3")
        else: self.size=size
        self.origin=(0,0,0)
        self.showing=False
        self.objects=dict()
    def addObj(self,obj):
        self.objects[obj.name]=obj
    def showObjects(self):
        return self.objects
    def createWorld(self):
        self.showing=True
