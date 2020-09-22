class Allergies:
    allergens = {
        128: "cats",
        64: "pollen",
        32: "chocolate",
        16: "tomatoes",
        8: "strawberries",
        4: "shellfish",
        2: "peanuts",
        1: "eggs",
    }

    def __init__(self, score):
        self.score = score
        self.allergic_list = [i for j, i in self.allergens.items() if self.score & j == j]

    def allergic_to(self, item):
        if item in self.lst:
            return True
        else:
            return False

    @property
    def lst(self):
        return self.allergic_list
