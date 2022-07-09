from typing import Tuple as t
class World:
    def __init__(self,dimension:int,size:t[float]):
        if dimension >3: raise
            self.dimension = dimension