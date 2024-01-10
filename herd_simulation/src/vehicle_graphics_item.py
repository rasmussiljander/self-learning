'''Creating a vehicle graphics item to be implemented into the GUI.'''

from PyQt5 import QtWidgets, QtGui,QtCore
from vector import Vector

class VehicleGraphicsItem(QtWidgets.QGraphicsPolygonItem):

    def __init__(self,vehicle):
        super(VehicleGraphicsItem,self).__init__()

        self.vehicle = vehicle
        self.setBrush(QtGui.QBrush(QtGui.QColor(255,0,0)))

        self.draw_triangle()
        self.update_all()

    '''The vehicle is triangle shaped so that its direction and movement is easier to follow.
        
        Here we are creating three different Q points and adding them to the QPOlygon we created.'''

    def draw_triangle(self):
        triangle = QtGui.QPolygonF()
        size = self.vehicle.size

        # Add the corners of a triangle to the the polygon object
        triangle.append(QtCore.QPointF(size, (size-10)/2))  # Tip (right)
        triangle.append(QtCore.QPointF(0, size-10))  # right corner (downwards)
        triangle.append(QtCore.QPointF(0,0))  # left corner (up)
        triangle.append(QtCore.QPointF(size, (size-10)/2))  # Tip

        # Set this newly created polygon as this Item's polygon.
        self.setPolygon(triangle)

        # Set the origin of transformations to the center of the triangle.
        # This makes it easier to rotate this Item.
        self.setTransformOriginPoint(size / 2, size / 2)


    '''for creating movement and autonomy for the vehicles. This is simple - we search the new value
        and the set it as the vehicle's new location or angle.'''

    def update_position(self):

        x = self.vehicle.x
        y = self.vehicle.y

        QtWidgets.QGraphicsItem.setPos(self,x,y)


    def update_rotation(self):

        dir_vec = self.vehicle.direction
        dir_deg = Vector.get_degrees(dir_vec)
        QtWidgets.QGraphicsItem.setRotation(self,dir_deg)

    def update_all(self):
        self.update_rotation()
        self.update_position()





