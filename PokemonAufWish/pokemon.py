class Pokemon:
    def __init__(self, PokemonId, name, level, typ, currentHp, maxHp, currentXp, needXpForLevelUp, attackList, stats):
        self.PokemonId = PokemonId
        self.name = name
        self.typ = typ
        self.level = level
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.currentXp = currentXp
        self.needXpForLevelUp = needXpForLevelUp
        self.attackList = attackList
        self.stats = stats




class PokemonAttacks:
    def __init__(self, AttackId, name, typ, baseDmg, baseAccuracy):
        self.AttackId = AttackId
        self.name = name
        self.typ = typ
        self.baseDmg = baseDmg
        self.baseAccuracy = baseAccuracy

    def weackness(self):
        pass