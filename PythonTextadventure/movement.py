import encounter
import random
import allTheFunctions

def forward():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")
        


def right():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")
def backwards():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")

def left():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")


