from re import M

from monster import Monster


class MonsterAttcks():
    def __init__(self, dmg, name, accuracy, critChance):
        self.dmg = dmg
        self.name = name
        self.accuarcy = accuracy
        self.critChance = critChance








bite = MonsterAttcks(35,"Biss", 100, 10)
sandAttack = MonsterAttcks(5,"Sandwirbel", 100, 0)
tackle = MonsterAttcks(30, "Tackle", 100, 20)
beakStitch = MonsterAttcks(40, "Schnabelstich", 90, 10)
clubAttack = MonsterAttcks(35, "Keulenhieb", 100, 10)


