import random

class Robot:

    def __init__(self):
        self.name = ""
        self.reset()

    def reset(self):
        random.seed()
        self.name = chr(random.randint(65, 90)) + \
        chr(random.randint(65, 90)) + \
        chr(random.randint(48, 57)) + \
        chr(random.randint(48, 57)) + \
        chr(random.randint(48, 57))
