import monster
import monsterAttacks as mA

wolf = monster.Monster(1, 1, "Wolf", 100, 100, 10, 10, [mA.bite, mA.tackle])
pig = monster.Monster(2, 1, "Schwein", 120, 120, 10, 10, [mA.bite, mA.tackle])
goblin = monster.Monster(3, 1, "Goblin", 120, 120, 12, 10, [mA.clubAttack, mA.tackle])
worge = monster.Monster(4, 1, "Worge", 150, 150, 15, 12, [mA.bite, mA.tackle])
snake = monster.Monster(5, 1, "Schlange", 100, 100, 10, 10, [mA.bite])
sheep = monster.Monster(6, 1, "Schaf", 50, 50, 0, 10, [mA.tackle])


level_1_monster = [wolf, pig, goblin, worge, snake, sheep]