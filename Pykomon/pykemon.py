
class Pykemon:
    def __init__(self, nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats):
        self.nummer = nummer
        self.name = name
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.currentXp = currentXp
        self.maxXp = maxXp
        self.listOfAttacks = listOfAttacks
        self.stats = stats





class FirePykemon(Pykemon):
    def __init__(self, nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats):
        super().__init__(nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats)
        self.type = "fire"
        self.weakness = "water"
        self.strengh = "grass"

class WaterPykemon(Pykemon):
    def __init__(self, nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats):
        super().__init__(nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats)
        self.type = "water"
        self.weakness = "grass"
        self.strengh = "fire"

class GrasPykemon(Pykemon):
    def __init__(self, nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats):
        super().__init__(nummer, name, currentHp, maxHp, currentXp, maxXp, listOfAttacks, stats)
        self.type = "grass"
        self.weakness = "fire"
        self.strengh = "water"