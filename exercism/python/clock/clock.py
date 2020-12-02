class Clock:
    def __init__(self, hour, minute):
        # could probably simplify this more but you know what. this is easier to read
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self):
        # zfill also works but i need to brush up on formatting
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return (self.hour == other.hour) and (self.minute == other.minute)

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
