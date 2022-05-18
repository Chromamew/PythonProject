from re import M
import monster
import monsterAttacks as mA

#Level1
wolf = monster.Monster(1, 1, "Wolf", 100, 100, 10, 10, [mA.bite, mA.tackle])
pig = monster.Monster(2, 1, "Schwein", 120, 120, 10, 10, [mA.bite, mA.tackle])
goblin = monster.Monster(3, 1, "Goblin", 120, 120, 12, 10, [mA.clubAttack, mA.tackle])
snake = monster.Monster(4, 1, "Schlange", 100, 100, 10, 10, [mA.bite])
sheep = monster.Monster(5, 1, "Schaf", 50, 50, 0, 10, [mA.tackle])


#level2
worge = monster.Monster(6, 2, "Worge", 150, 150, 15, 12, [mA.bite, mA.tackle])
molerat = monster.Monster(7, 2, "Molerat", 200, 200, 10, 10, [mA.bite, mA.tackle])
scavenger = monster.Monster(8, 2, "Scavenger", 150, 150, 15, 12, [mA.bite, mA.tackle])

#level3

waran = monster.Monster(9, 3, "Waran", 200, 200, 20, 20, [mA.bite, mA.tackle, mA.sandAttack])
lurker = monster.Monster(10, 3, "Lurker", 180, 180, 18, 18, [mA.bite, mA.tackle])
water_golem = monster.Monster(11, 3, "Wassergolem", 250, 250, 25, 10, [mA.clubAttack])
fire_golem = monster.Monster(11, 3, "Feuergolem", 250, 250, 25, 10, [mA.clubAttack])
stone_golem = monster.Monster(11, 3, "Steingolem", 250, 250, 25, 10, [mA.clubAttack])





level_1_monster = [wolf, pig, goblin, snake, sheep]
level_2_monster = [worge, molerat, scavenger]
level_3_monster = [waran, lurker, water_golem, fire_golem, stone_golem]