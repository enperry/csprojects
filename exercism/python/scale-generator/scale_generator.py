SHARPS = ['C', 'a', 'G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
SHARP_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
FLAT_SCALE = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.scale = SHARP_SCALE if self.tonic in SHARPS else FLAT_SCALE

    def chromatic(self):
        tonic = self.tonic.capitalize()
        tonic_index = self.scale.index(tonic)
        return self.scale[tonic_index:] + self.scale[:tonic_index]

    def interval(self, intervals):
        c_scale = self.chromatic()
        steps = intervals.replace("m", "1").replace("M", "2").replace("A", "3")
        output = []

        pos = 0
        for step in steps:
            output.append(c_scale[pos])
            pos = pos + int(step)
        return output