from random import randint

abilities = ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma")

def modifier(constitution):
    return (constitution - 10) // 2

class Character:
    def __init__(self):
        for ability in abilities:
            setattr(self, ability, self.ability())
        self.constMod = modifier(self.constitution)
        self.hitpoints = self.constMod + 10

    def ability(self):
        fullList = [randint(1, 6) for _ in range(4)]
        fullList.remove(min(fullList))
        return sum(fullList)