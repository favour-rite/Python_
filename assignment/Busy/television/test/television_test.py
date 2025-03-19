import unittest
from television.Television import Television
from television.exception import *

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

    def test_initial_state(self):
        self.assertFalse(self.tv.get_is_on(), False)
        self.assertEqual(self.tv.get_volume(), 0)
        self.assertEqual(self.tv.get_channel(), 0)

    
    def test_television_is_turn_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on(),True)

    def test_television_is_turn_off(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on(), True)
        self.tv.turn_off()
        self.assertFalse(self.tv.get_is_on(), False)

    def test_that_television_increase_volume(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on())
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.assertEqual(self.tv.get_volume(), 2)

    def test_that_television_decrease_volume(self):
        self.tv.turn_on()
        self.tv.increase_volume()
        self.tv.increase_volume()
        self.assertEqual(self.tv.get_volume(), 2)
        self.tv.decrease_volume()
        self.assertEqual(self.tv.get_volume(), 1)

    def test_channel_up_when_tv_is_on_and_within_range(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on())

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 3)

    def test_channel_down_when_tv_is_on_and_within_range(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.get_is_on())

        self.tv.channel_up()
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 2)
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel(), 1)

    def test_channel_up_when_tv_is_off(self):
        self.tv.turn_off()
        with self.assertRaises(Exception):
            self.tv.channel_up()

    def test_channel_down_when_tv_is_off(self):
        self.tv.turn_off()
        with self.assertRaises(Exception):
            self.tv.channel_down()

    def test_television_volume_can_be_increased_when_turn_off(self):
        self.tv.turn_off()
        with self.assertRaises(Exception):
            self.tv.increase_volume()

    def test_television_volume_can_be_decreased_when_turn_off(self):
        self.tv.turn_off()
        with self.assertRaises(Exception):
            self.tv.decrease_volume()





    # def test_that_television_volume_is_muted(self):
    #     self.tv.turn_on()
    #     self.assertTrue(self.tv.get_is_on())
    #     self.tv.increase_volume()
    #     self.tv.increase_volume()
    #     self.assertEqual(self.tv.get_volume(), 2)
    #     self.tv.mute()
    #     self.assertEqual(self.tv.get_volume(), 0)

    # def test_that_television_volume_is_un_muted(self):
    #     self.tv.turn_on()
    #     self.assertTrue(self.tv.get_is_on())
    #     self.tv.increase_volume()
    #     self.tv.increase_volume()
    #     self.assertEqual(self.tv.get_volume(), 2)
    #     self.tv.mute()
    #     self.assertEqual(self.tv.get_volume(), 0)
    #     self.tv.unmute()
    #     self.assertEqual(self.tv.get_volume(), 2)
if __name__ == '__main__':
    unittest.main()
