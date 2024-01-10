'''Class for creating a path for a vehicle to follow. Each vehicle is given their own path with a particular start, end,
and radius'''

from vector import Vector

class Path:

    def __init__(self,start, finish):

        self.start_coors = start
        self.finish_coors = finish

        self.radius = 20        #arbitrary testing value

        self.start = self.start_into_vector()
        self.finish = self.finish_into_vector()

        self.vec = self.finish.sub(self.start)



    '''Creating method to change coordinates into vector.'''

    def start_into_vector(self):
        x = self.start_coors[0]
        y = self.start_coors[1]
        return Vector(x,y)

    def finish_into_vector(self):
        x = self.finish_coors[0]
        y = self.finish_coors[1]
        return Vector(x,y)



