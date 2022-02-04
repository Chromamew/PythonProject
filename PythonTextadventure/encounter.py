import imp


import random
import allTheMonster as monster

def encounter_Monster(beginn, end):
    
    if random.randrange(beginn, end) >= 5:
        enemy_monster = choose_monster()

def choose_monster():
    random.choice(monster.level_1_monster)
