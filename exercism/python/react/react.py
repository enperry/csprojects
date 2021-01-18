class InputCell:
    def __init__(self, initial_value):
        self.__value = initial_value
        self.__subscribers = []

    def subscribe(self, compute_cell):
        if(compute_cell not in self.__subscribers):
            self.__subscribers.append(compute_cell)
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
        for subscriber in self.__subscribers:
            subscriber.update()


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.__inputs = inputs
        self.__callbacks = []
        self.__compute_function = compute_function
        self.value = self.compute_value()
        self.subscribe(self)

    def subscribe(self, compute_cell):
        for _input in self.__inputs:
            _input.subscribe(compute_cell)

    def compute_value(self):
        inputs = list(map(lambda input: input.value, self.__inputs))
        return self.__compute_function(inputs)
            
    def update(self):
        last_value = self.value
        self.value = self.compute_value()
        if(self.value != last_value):
            for callback in self.__callbacks:
                callback(self.value)

    def add_callback(self, callback):
        self.__callbacks.append(callback)
    
    def remove_callback(self, callback):
        if(callback in self.__callbacks):
            self.__callbacks.remove(callback)