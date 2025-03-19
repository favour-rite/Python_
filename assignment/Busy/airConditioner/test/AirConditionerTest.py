import unittest
from airConditioner.AirConditioner import AirConditioner

class AirConditionerTest(unittest.TestCase):

    def setUp(self):
        self.airConditioner = AirConditioner()

    def test_initial_state_of_the_air_conditioner(self):
        self.assertEqual(self.airConditioner.get_is_on(), False)
        self.assertEqual(self.airConditioner.get_temperature(),16)


    def test_air_conditioner_turn_on(self):
        self.airConditioner.turn_on()

        self.assertTrue(self.airConditioner.get_is_on(),"Air Conditioner is on")

    def test_air_conditioner_turn_off(self):
        self.airConditioner.turn_off()
        self.assertFalse(self.airConditioner.get_is_on(),"Air Conditioner is off")


    def test_air_conditioner_set_temperature(self):
        self.airConditioner.turn_on()
        self.assertTrue(self.airConditioner.get_is_on(),"Air Conditioner is on")
        self.assertEqual(self.airConditioner.set_temperature(16),"increase by one")
        self.airConditioner.increase_temperature(17)
        self.assertEqual(self.airConditioner.get_temperature(),17)
        self.assertEqual(self.airConditioner.get_temperature(),"Temperature is set to 25")

    # def test_air_conditioner_cannot_be_decrease_temperature_when_off(self):
    #     self.airConditioner.turn_off()
    #     self.airConditioner(self.airConditioner.get_is_on(), "Air Conditioner is off")
    #     self.airConditioner.decrease_temperature(17)
    #     self.assertEqual(self.airConditioner.get_temperature(), 16, "Temperature is set back to it initial state 16")
    #
    # # def test_air_conditioner_cannot_set_temperature_below_16(self):
    #     self.airConditioner.turnOn()
    #     self.airConditioner(self.airConditioner.get_mode(), True,"Air Conditioner is on")
    #     self.airConditioner.set_temperature(15)
    #     self.assertEqual(self.airConditioner.get_temperature(), 16,"Temperature is set back to it initial state 16")