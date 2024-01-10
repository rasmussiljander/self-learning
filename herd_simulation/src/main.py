# Main-module for running the classes and program

import sys, random
from PyQt5.QtWidgets import QApplication

from gui import GUI
from vector import Vector
from vehicle import Vehicle
from vehicle_world import VehicleWorld
from car_info_file_error import CarInfoFileError

"""This is where the entire program is run. First we must read a csv file where the information for the cars are set up,
in the order of "number of cars, car size, Force to mass ratio (FM) range, location ranges, max speed range. There are 
restrictions that are checked (come up with empirical experimentation):
    1 <= number of cars <= 15
    30 <= car size <= 50
    finish location cannot be in the center of the window
    1 <= max speed <= 2.5"""


def load_game(filename):
    world = VehicleWorld()  # creating a test world

    try:
        file_open = open(filename, "r")

    except FileNotFoundError:
        raise CarInfoFileError("Invalid file!")

    except OSError:
        raise CarInfoFileError("Invalid file!")

    file = file_open.readlines()
    file_open.close()
    file = [file[i] for i in range(len(file)) if file[i] != "\n"]
    info = file[2].split(",")
    info = check_input(info)  # list of parameters for setting up the car.

    n_cars = int(info[0])  # number of cars
    size = info[1]  # car size (pixels)

    for i in range(n_cars):
        fm = random.uniform(info[2], info[3])  # steering constant force/mass

        success = 0
        while success == 0:
            # randomly generating x,y coordinates
            start = [random.uniform(info[4], info[5]) for i in range(2)]
            finish = [random.uniform(info[4], info[5]) for i in range(2)]

            # if path is too short or the the vehicles end up on top of each other
            if check_path_length(start, finish) < 650 or check_overlap(finish, world) != 0:
                success = 0
            else:
                success += 1

        direction = Vector((finish[0] - start[0]), (finish[1] - start[1])).get_unit()
        path = [start, finish]
        max_speed = random.uniform(info[6], info[7])

        # creating a car-object and adding it to the world
        car = Vehicle(fm, max_speed, direction, path, size, world)
        world.add_vehicle(car)

    app = QApplication(sys.argv)  # initializing the GUI.
    wind = GUI(world)

    sys.exit(app.exec())


"""CHECK PATH LENGTH:
    Calculates the length of the path, a.k.a the distance between the start point and the finish point. Parameters as a 
    list (e.g. start = [start x coordinate, start y coordinate])"""


def check_path_length(start, finish):
    start_v = Vector(start[0], start[1])  # make list values into vectors
    finish_v = Vector(finish[0], finish[1])

    path = finish_v.sub(start_v)
    return path.get_magn()


"""CHECK OVERLAP
Checks whether finishing points between cars are too close to each other, i.e. if they overlap when they stop. If they do
a number other than 0 is returned."""


def check_overlap(finish, world):
    vehicles = world.get_vehicles()  # list of cars
    overlap = 0
    for i in range(len(vehicles)):
        other_finish = vehicles[i].target  # finishing location of other car
        if (
            check_path_length(other_finish, finish) < 50
        ):  # finishing locations are too close to each other
            overlap += 1

    return overlap


"""CHECK INPUT
Method for checking if the input in the the given file is valid. Checks all numbers, values, etc. to see if the file is written 
against the instructions given. If so, an error is risen."""


def check_input(list):
    try:
        # list of parameters for setting up the car.
        info = [float(list[i]) for i in range(len(list))]

        if len(info) != 8:
            raise CarInfoFileError("Something wrong about the info!")

        n_cars = int(info[0])  # number of cars

        if n_cars == 0:
            raise CarInfoFileError(
                "{} is an invalid amount of cars! Should be more than 0".format(n_cars)
            )

        if info[1] < 30 or info[1] > 50:
            raise CarInfoFileError(
                "{} is an invalid car size! Should be within 30 and 50.".format(info[1])
            )

        if info[2] < 0.05 or info[2] > 0.2:
            raise CarInfoFileError(
                "{}-{} invalid force/mass range! Min: 0.05, Max: 0.2".format(info[2], info[3])
            )

        if info[3] < info[2] or info[3] > 0.2:
            raise CarInfoFileError(
                "{}-{} invalid force/mass range! Min: 0.05, Max: 0.2".format(info[2], info[3])
            )

        if info[4] < 50 or info[4] > 750:
            raise CarInfoFileError("Invalid range of coordinates.")
        if info[4] > info[5] or info[5] <= 50 or info[5] > 750:
            raise CarInfoFileError("Invalid range of coordinates.")

        if info[6] > info[7] or info[6] < 0.75 or info[7] > 2.5:
            raise CarInfoFileError(
                "{}-{} is an incorrect range for max speed!. Should be 0.75-2.50".format(
                    info[10], info[11]
                )
            )
        return info

    # If any of info inputs are invalid (characters, etc.) a valueError is raised
    except ValueError:
        raise CarInfoFileError("Invalid car info input! Please give only numbers.")


if __name__ == "__main__":
    load_game("car_info.csv")
