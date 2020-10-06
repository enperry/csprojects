from collections import deque

class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):
    pass

class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = deque([], maxlen = capacity)

    def read(self):
        if(len(self.buffer) > 0):
            return self.buffer.popleft()
        else: 
            raise BufferEmptyException("Circular buffer is empty.")

    def write(self, data):
        if(len(self.buffer) < self.buffer.maxlen):
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full.")

    def overwrite(self, data):
        if(len(self.buffer) == self.buffer.maxlen):
            self.read()
        self.write(data)

    def clear(self):
        self.buffer.clear()