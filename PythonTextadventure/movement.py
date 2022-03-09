import encounter
import random
import allTheFunctions

def forward():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
        allTheFunctions.nextStep()
        


def right():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)
def backwards():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)

def left():
    if random.randrange(0, 10) > 5:
        enemyMonster= encounter.chooseMonster()
        print(enemyMonster.name)


