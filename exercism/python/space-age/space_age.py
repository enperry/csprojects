class SpaceAge:
    planetYears = {
        "earth": 1.0,
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.age = seconds / 31557600

    def calcAge(self, planet):
        return round(self.age / self.planetYears[planet], 2)

    def on_earth(self):
        return self.calcAge("earth")

    def on_mercury(self):
        return self.calcAge("mercury")

    def on_venus(self):
        return self.calcAge("venus")

    def on_mars(self):
        return self.calcAge("mars")

    def on_jupiter(self):
        return self.calcAge("jupiter")

    def on_saturn(self):
        return self.calcAge("saturn")

    def on_uranus(self):
        return self.calcAge("uranus")

    def on_neptune(self):
        return self.calcAge("neptune")