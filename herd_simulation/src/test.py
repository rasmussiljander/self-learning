"""TEST CLASS
Below are unittests for testing whether the tests and code are valid."""

from car_info_file_error import CarInfoFileError
import unittest
import csv
from vector import Vector
from main import load_game, check_input, check_path_length, check_overlap
import math
from path import Path
from vehicle import Vehicle
from vehicle_world import VehicleWorld


class TestInput(unittest.TestCase):
    """A test case class for testing the input validation function."""

    def test_bad_numbers(self):
        """Tests bad input numbers."""
        self.perfect_input = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]

        self.zero_cars = [
            "0",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.zero_cars)

        self.not_all_info = [
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.not_all_info)

        self.invalid_size = [
            "2",
            "60",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.invalid_size)

        self.fm_too_small = [
            "3",
            "40",
            "0.01",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.fm_too_small)

        self.fm_too_big = [
            "3",
            "40",
            "0.05",
            "0.22",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.fm_too_big)

        self.writing = [
            "3",
            "40",
            "asdf",
            "rasd",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.writing)

        self.lower_bound_bad = [
            "3",
            "40",
            "0.05",
            "0.2",
            "10",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.lower_bound_bad)

        self.upper_bound_bad = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "800",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.upper_bound_bad)

        self.upper_is_lower = [
            "3",
            "40",
            "0.05",
            "0.2",
            "650",
            "100",
            "50",
            "100",
            "600",
            "650",
            "1",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.upper_is_lower)

        self.max_speed_low = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "0.5",
            "2.5",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.max_speed_low)

        self.max_speed_high = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "1",
            "3",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.max_speed_high)

        self.max_speed_high_is_low = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "2",
            "1",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.max_speed_high_is_low)

        self.last_text = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "2",
            "rs",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.last_text)

        self.secondlast_text = [
            "3",
            "40",
            "0.05",
            "0.2",
            "50",
            "750",
            "50",
            "100",
            "600",
            "650",
            "r",
            "2",
        ]
        self.assertRaises(CarInfoFileError, check_input, self.secondlast_text)

    def test_returns_list(self):
        self.returnable = [3, 40, 0.05, 0.2, 50, 750, 1, 2.5]
        self.perfect_input = ["3", "40", "0.05", "0.2", "50", "750", "1", "2.5"]

        self.assertEqual(self.returnable, check_input(self.perfect_input))


class TestGameLoad(unittest.TestCase):
    """A test case class for testing the game load function."""

    def setUp(self):
        """Initialize the game"""
        self.titles = [
            "Number of Cars",
            "Car size",
            "FM L",
            "FM U",
            "Coordinates L",
            "Coordinates U",
            "max speed l",
            "max speed u",
        ]

        self.header = ["Below the parameters for the simulated cars are set up."]

        self.numbers = ["2", "40", "0.05", "0.2", "50", "750", "1", "2.5"]

    def test_missing_header_or_titles_or_info(self):
        """Tests if the header, titles, or info is missing."""
        self.missing_header = [self.titles, self.numbers]
        with open("missing_header.csv", "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.missing_header)

        csvFile.close()
        self.assertRaises(IndexError, load_game, "missing_header.csv")

        csvFile.close()

    def test_ncars_and_size(self):
        """Tests if the number of cars and the size is correct."""
        self.file = [self.header, self.titles, self.numbers]

        with open("ncars_size.csv", "w") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.file)

        csvFile.close()

        file_open = open("ncars_size.csv", "r")
        file = file_open.readlines()
        file_open.close()
        file = [file[i] for i in range(len(file)) if file[i] != "\n"]
        info = file[2].split(",")

        info = check_input(info)  # list of parameters for setting up the car.

        self.assertEqual(info[0], 2)

        self.assertEqual(info[1], 40)

    """self.missing_titles = [['Below the parameters for the simulated cars are set up.'],
            ['0', '40', '0.05', '0.2', '50', '750', '50', '100', '600', '650','1', '2.5']]

        with open('missing_titles.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.missing_header)

        csvFile.close()
        #self.assertRaises(IndexError, load_game, "car_info.csv")"""

    def test_load_game(self):
        """test load_game function"""
        self.assertRaises(CarInfoFileError, load_game, "rass")

        self.assertRaises(CarInfoFileError, load_game, 342)

    def test_path_length(self):
        """test path length function"""
        v1 = [7, 5]
        v2 = [4, 1]
        self.assertEqual(check_path_length(v1, v2), 5)


class TestVector(unittest.TestCase):
    """A test case class for testing the vector class. Tests for adding, subtracting, multiplying, getting magnitude, etc."""

    def test_length(self):
        """Test the length of a vector"""
        self.assertEqual(math.hypot(3, 4), 5, "Should be 5")

    def test_get_unit_from_zero(self):
        """Test getting the unit vector from a zero vector"""
        self.assertEqual(Vector(0, 0).get_unit().get_magn(), Vector(0, 0).get_magn())

    def test_set_magn(self):
        """Test setting the magnitude of a vector"""
        self.assertEqual(round(Vector(0, 0).set_magn(3).get_magn(), 5), 3, "should be 3")

    def test_set_magn_zero(self):
        """Test setting the magnitude of a vector to zero"""
        self.assertEqual(Vector(3, 3).set_magn(0).get_magn(), 0, "Should be zero")

    def test_get_magn(self):
        """Test getting the magnitude of a vector"""
        self.assertEqual(Vector(3, 4).get_magn(), 5, "Should be 5")

    def test_return_degrees(self):
        """Test returning the angle of a vector in degrees"""
        self.assertEqual(Vector(0, 2).get_degrees(), 90, "Should be 45")

    def test_correct_angle(self):
        """Test calculating the correct angle of a vector"""
        self.assertEqual(round(math.atan2(1, 1), 4), 0.7854, "should be 0.78...")

    def test_adding(self):
        """Test adding two vectors"""
        a = Vector(1, 3)
        b = Vector(2, 1)
        self.assertEqual(a.add(b).get_magn(), 5)

    def test_sub(self):
        """Test subtracting two vectors"""
        a = Vector(7, 5)
        b = Vector(3, 2)
        self.assertEqual(a.sub(b).get_magn(), 5)

    def test_mult(self):
        """Test multiplying a vector by a scalar"""
        self.assertEqual(Vector(1.5, 2).mult(2).get_magn(), 5)

    def test_set_limit_magn_smaller(self):
        """Test setting the magnitude limit of a vector to a smaller value"""
        self.assertEqual(Vector(2, 2).set_limit(1).get_magn(), 1)

    def test_set_limit_magn_bigger(self):
        """Test setting the magnitude limit of a vector to a bigger value"""
        self.assertEqual(Vector(3, 4).set_limit(10).get_magn(), 5)

    def test_dot_product(self):
        """Test calculating the dot product of two vectors"""
        self.assertEqual(Vector(1, 2).dot_product(Vector(3, 4)), 11)

    def test_get_x(self):
        """Test getting the x-coordinate of a vector"""
        self.assertEqual(Vector(1, 0).get_x(), 1)

    def test_get_y(self):
        """Test getting the y-coordinate of a vector"""
        self.assertEqual(Vector(0, 1).get_y(), 1)


class TestPath(unittest.TestCase):
    """Test class for Path Class"""

    def setUp(self):
        self.start = [3, 4]
        self.finish = [5, 12]

    def test_start_vec(self):
        self.assertEqual(Path(self.start, self.finish).start_into_vector().get_magn(), 5)

    def test_finish_vec(self):
        self.assertEqual(Path(self.start, self.finish).finish_into_vector().get_magn(), 13)


class TestVehicle(unittest.TestCase):
    """Test case for the Vehicle class."""

    def setUp(self):
        """Set up the test environment."""
        self.path = [[0, 0], [3, 4]]
        self.world = VehicleWorld()
        self.fm = 0.1
        self.max_speed = 1.5
        self.direction = Vector(1, 1).get_unit()
        self.vehicle = Vehicle(self.fm, self.max_speed, self.direction, self.path, 30, self.world)
        self.world.add_vehicle(self.vehicle)

    def test_fm(self):
        """Test the fm (force)  attribute of the vehicle."""
        self.assertEqual(self.fm, self.vehicle.fm)

    def test_overlap_from_main(self):
        """Test the check_overlap function from the main module."""
        path2 = [[0, 0], [5, 5]]
        vehicle2 = Vehicle(self.fm, self.max_speed, self.direction, path2, 30, self.world)
        self.world.add_vehicle(vehicle2)

        self.assertEqual(check_overlap(self.path[1], self.world), 2)


if __name__ == "__main__":
    unittest.main()
