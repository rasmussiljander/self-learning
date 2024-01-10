''' Information about the world that the vehicles are placed in. Using this class we can easily keep track of the amount
vehicles in this world '''

#from vehicle import Vehicle

class VehicleWorld:


    def __init__(self):
        self.vehicles = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)


    def get_vehicles(self):
        return self.vehicles
