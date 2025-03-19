from exception import SpeedErrorException


class Automatic_bike:

    def __init__(self):

        self.is_on = False
        self.speed = 0
        self.gear = 15
    
    @property
    def get_is_on(self):
        return self.is_on

    @property
    def get_speed(self):
        return self.speed
    
    @property
    def get_gear(self):
        return self.gear
    
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_speed(self, speed):
        self.speed = speed

    def accelerate_bike_speed_according_to_gear(self):
        if self.is_on and self.speed == 15 and self.gear == 1:
            self.speed += 1
        elif self.speed == 24 and self.gear == 2:
            self.speed += 2
        elif self.speed == 35 and self.gear == 3:
            self.speed += 3
        elif self.speed == 44 and self.gear == 4:
            self.speed += 4
        else:
            raise SpeedErrorException("Speed should not be beyond the gear")
        return self.speed
    
    def deaccelerate_bike_speed_according_to_gear(self):
        if self.is_on and self.speed == 15 and self.gear == 1:
            self.speed -= 1
        elif self.speed == 24 and self.gear == 2:
            self.speed -= 2
        elif self.speed == 35 and self.gear == 3:
            self.speed -= 3
        elif self.speed == 44 and self.gear == 4:
            self.speed -= 4
        else:
            raise SpeedErrorException("Speed should not be beyond the gear")
        return self.speed
    
    def change_gear(self, gear):
        self.gear = gear
        return self.gear
    

