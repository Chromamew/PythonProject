import encounter
import random
import allTheFunctions


#REFACTOR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def forward():
    if random.randrange(0, 10) > 5:
        enemyMonster = encounter.chooseMonster()
        print(f"Du begegnest einer/einem {enemyMonster.name}")
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")

def right():
    if random.randrange(0, 10) > 5:
        enemyMonster = encounter.chooseMonster()
        print(f"Du begegnest einer/einem {enemyMonster.name}")
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")
def backwards():
    if random.randrange(0, 10) > 5:
        enemyMonster = encounter.chooseMonster()
        print(f"Du begegnest einer/einem {enemyMonster.name}")
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")

def left():
    if random.randrange(0, 10) > 5:
        enemyMonster = encounter.chooseMonster()
        print(f"Du begegnest einer/einem {enemyMonster.name}")
        allTheFunctions.nextStep()
    else:
        print("Nichts ist passiert")


