class CustomSet:
    def __init__(self, elements = None):
        if(elements):
            self._elements = elements
        else:
            self._elements = []

    def isempty(self):
        return len(self._elements) == 0

    def __contains__(self, element):
        return element in self._elements

    def issubset(self, other):
        return all([(x in other) for x in self._elements])

    def isdisjoint(self, other):
        return all([not (x in other) for x in self._elements])

    def __eq__(self, other):
        return self.issubset(other) and other.issubset(self)

    def add(self, element):
        if(element not in self._elements):
            self._elements.append(element)

    def intersection(self, other):
        return CustomSet([x for x in self._elements if x in other])

    def __sub__(self, other):
        return CustomSet([x for x in self._elements if not (x in other)])

    def __add__(self, other):
        return CustomSet(self._elements + [x for x in other if x not in self._elements])

    def __repr__(self):
        return f'{self._elements}'

    def __iter__(self):
        return self._elements.__iter__()