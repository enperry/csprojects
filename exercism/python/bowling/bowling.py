class BowlingGame:
    def __init__(self):
        self.frames = []

    def roll(self, pins):
        if(not -1 < pins < 11):
            raise ValueError("invalid number of pins")

        # first throw
        if(len(self.frames) == 0):
            self.frames.append([pins])

        elif(len(self.frames[-1]) == 1):
            # strike
            if(self.frames[-1][0] == 10):
                if(len(self.frames) < 10):
                    self.frames.append([pins])
                else:
                    # bonus roll after strike
                    self.frames[-1].append(pins)
            # otherwise
            elif(self.frames[-1][0] + pins > 10):
                raise ValueError("can't score more than 10 points in a frame")
            else:
                self.frames[-1].append(pins)
        elif(len(self.frames[-1]) == 2):
            if(len(self.frames) < 10):
                self.frames.append([pins])
            # Bonus balls in last frame
            elif(sum(self.frames[-1]) < 10):
                raise ValueError("no bonus ball")
            elif(self.frames[-1][0] == 10 and self.frames[-1][1] != 10 and self.frames[-1][1] + pins > 10):
                raise ValueError("can't score more than 10 points after strike")
            else:
                self.frames[-1].append(pins)
        else:
            raise ValueError("no more balls")

    def score(self):
        total = 0
        # add spares
        for i in range(9):
            l = len(self.frames[i])
            s = sum(self.frames[i])
            if(s < 10):
                total = total + s
            # spare
            elif(l == 2):
                total = total + (s + self.frames[i + 1][0])
            # strike
            elif(l == 1 and len(self.frames[i + 1]) == 2):
                total = total + (s + sum(self.frames[i + 1]))
            else:
                if(i < 8):
                    total = total + (s + self.frames[i + 1][0] + self.frames[i + 2][0])
                else:
                    total = total + (s + self.frames[i + 1][0] + self.frames[i + 1][1])


        total = total + sum(self.frames[9])

        return total