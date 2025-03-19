import unittest
from bike.Automatic_bike import Automatic_bike
from bike.exception import SpeedErrorException

class AutomaticBike_Test(unittest.TestCase):

    def setUp(self):
        self.bike = Automatic_bike()

    def test_bike_initial_state(self):
        self.assertEqual(self.bike.get_is_on(), False, "initial state of BIKE: Bike should be turned off")
        self.assertEqual(self.bike.get_speed(), 0, "Speed should be 0")
        self.assertEqual(self.bike.get_gear(), 1, "Gear should be 1")

    def test_bike_is_turned_on(self):
        self.bike.turn_on()
        self.assertEqual(self.bike.get_is_on(), True, "Bike should be turned on")

    def test_bike_is_turned_off(self):
        self.bike.turn_on()
        self.assertEqual(self.bike.get_is_on(), True, "Bike should be turned on")
        self.bike.turn_off()
        self.assertEqual(self.bike.get_is_on(), False, "Bike should be turned off")

    def test_that_automatic_bike_is_accerlerated_according_to_gear(self):
        self.bike.turn_on()
        self.assertEqual(self.bike.get_is_on(), True, "Bike should be turned on")
        self.bike.set_speed(15)
        self.bike.change_gear(1)
        self.bike.accelerate_bike_speed_according_to_gear()
        self.assertEqual(self.bike.get_speed(), 16, "Speed should not be beyond the gear: start from 15")

    def test_that_automatic_bike_is_deaccelerated_according_to_gear(self):
        self.bike.turn_on()
        self.assertEqual(self.bike.get_is_on(), True, "Bike should be turned on")
        self.bike.set_speed(15)
        self.bike.change_gear(1)
        self.bike.deaccelerate_bike_speed_according_to_gear()
        self.assertEqual(self.bike.get_speed(), 14, "Speed should not be beyond the gear: start from 15")
