class TemperatureIsTooLow(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Temperature is too low: " + str(self.temperature)
    
class TemperatureIsTooHigh(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "Temperature is too high: " + str(self.temperature)