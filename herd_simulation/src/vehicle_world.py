""" Information about the world that the vehicles are placed in. Using this class we can easily keep track of the amount
vehicles in this world """

# from vehicle import Vehicle


class VehicleWorld:
    """
    Represents a world that contains vehicles.
    """

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """
        Adds a vehicle to the world.

        Args:
            vehicle: The vehicle to be added.
        """
        self.vehicles.append(vehicle)

    def get_vehicles(self):
        """
        Returns the list of vehicles in the world.

        Returns:
            A list of vehicles.
        """
        return self.vehicles
