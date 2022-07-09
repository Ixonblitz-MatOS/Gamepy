from exceptions import exc
import World as w
class Camera(object):
    def __init__(self,world:w.World,name:str,dimension:int,position:(int,int,int),active:bool):
        self.name=name
        self.world=world
        super().__init__()
        if dimension >3 or dimension <2: exc.raiseCamera("Dimension must be 2 or 3")
        else:
            if(len(position)!=dimension):exc.raiseCamera("Dimension and position dimensions don't match")
            else:pass
        self.dimension=dimension
        self.pos=position
        #Setting viewpoint of camera
        lst1=list()#begin
        lst2=list()#end
        for i in self.pos:
            lst1.append(i-60)
        for i in self.pos:
            lst2.append(i+60)
        self.view={tuple(lst1):tuple(lst2)}#60 pixels below and above
        self.active=active
        self.settings={"active":active,"position":position}
    def setActive(self,status:bool):
        self.active=status
        self.update()
    def update(self):
        for i in self.settings:
