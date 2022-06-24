class Monster:
    def __init__(self, id, level, name, currentHp, maxHp, dmg, speed, attackList):
        self.id = id
        self.level = level
        self.name = name
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.dmg = dmg
        self.speed = speed
        self.attackList = attackList