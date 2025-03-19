
from television import exception
from television.exception import VolumeIsHighException, VolumeIsLowException, ChannelIsIncreasedException, \
    ChannelIsDecreasedException, TelevisionIsMutedException, TelevisionIsUnmutedException


class Television:
    
    def __init__(self):

        self.is_on = False
        self.volume = 0
        self.channel = 0

    def get_is_on(self):
        return self.is_on
    def get_volume(self):
        return self.volume
    def get_channel(self):
        return self.channel

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def increase_volume(self):

        if self.get_is_on() and self.volume < 100:
            self.volume += 1
        elif self.volume > 100:
            raise VolumeIsHighException("Volume is out of range")
    def decrease_volume(self):

        if self.get_is_on() and self.volume > 0:
            self.volume -= 1
        elif self.volume < 0:
            raise VolumeIsLowException("Volume is out of range")


    def channel_up(self):

        if self.get_is_on():
            if self.channel < 100:
                self.channel += 1
            else:
                raise ChannelIsIncreasedException("Channel cannot go above 100")
        else:
                raise Exception("TV is off. Cannot change channel")

    def channel_down(self):

        if self.get_is_on():
            if self.channel > 1:
                self.channel -= 1
            else:
                raise ChannelIsDecreasedException("Channel cannot go below 1")
        else:
                raise Exception("TV is off. Cannot change channel")

    # def mute(self):
    #     if not self.get_is_on():
    #         self.volume = 0
    #     else:
    #         raise TelevisionIsMutedException("Television volume is muted")
    #     return self.volume

    # def unmute_television_volume_when_it_turned_on(self):
    #     if self.get_is_on():
    #
    #         raise TelevisionIsUnmutedException("Television volume is un muted")
    #     return self.volume










