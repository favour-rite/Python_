from airConditioner.Exception import TemperatureIsTooLow


class AirConditioner:

    def __init__(self):
        self.is_on = False
        self.__temperature = 16

    def get_is_on(self):
        return self.is_on

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def increase_temperature(self, temperature):
        for count in range(16, 34):
            if self.is_on and temperature > 16:
                self.set_temperature(temperature + count)
            elif self.is_on and temperature < 16:
                raise TemperatureIsTooLow("it looks like it's too high")


    def decrease_temperature(self, param):
        pass





