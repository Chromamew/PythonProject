from player import Player
from pykemon import FirePykemon, WaterPykemon, GrasPykemon

me = Player("Unbekannt")
gameLoop = True


# Intro
def intro():
    print(
        "Willkommen Fremder.\nDu bist hier in der Welt der PYKEMON.\nMein Name ist S.Eich. und ich erkläre dir diese Welt.")

    me.name = input("Doch bitte sag mir wie dein Name lautet!\n>")
    if me.name == "":
        print(
            "Gut dann verrate mir Deinen anmen nicht. Im laufe des Spiels kannst du ihn gegen Geld noch ändern lassen")
    else:
        print(f"Schön dich kennen zu lernen {me.name}.")

    print(
        "Also...\nDu bekommst von mir dein erstes PYKEMON und Deine Aufgabe wird es sein alle PYKEMON in dieser Welt zu finden und zu fangen.\n"
        "Du musst Kämpfe gegen andere PYKEMON-Trainer bestreiten oder wilde PYKEMON besiegen damit deine PYKEMON stärker werden.\n"
        "In jeder Stadt kannst du einen Arenaleiter herausfordern, solltest Du sie besiegen, bekommst du einen Orden.\n"
        "Hast du alle 8 Orden gesammelt, kannst du die TOP 4 herausfordern. Doch sei Dir bewusst, sie heißen nicht um sonst die TOP 4.")


def chooseFirstPykemon(me):
    print("Ich habe hier 3 PYKEMON für dich zur verfügung. Mit welchem davon möchtest du deine Reise beginnen?")
    bulbasaur = GrasPykemon(1, "Bisasam", 100, 100, 0, 100, [], [])
    charmander = FirePykemon(4, "Glumanda", 100, 100, 0, 100, [], [])
    squirtle = WaterPykemon(1, "Schiggy", 100, 100, 0, 100, [], [])
    userinput = input(f"  1.{bulbasaur.name}\n  2.{charmander.name}\n  3.{squirtle.name}\n  >")
    if userinput == "1":
        me.currentFrontPykemon = bulbasaur
        print("Schön. Du hast dich für Bisasam entschieden, das ist ein niedliches Pflanze PYKEMON")
    elif userinput == "2":
        me.currentFrontPykemon = charmander
        print("Sehr schön. Du hast dich für Glumanda entschieden, das ist ein starkes Feuer PYKEMON")
    elif userinput == "3":
        me.currentFrontPykemon = squirtle
        print("Schön. Du hast dich für Schiggy entschieden, das ist ein beeindrukendes Wasser PYKEMON")
    else:
        print("Bitte gibt eine zahl zwischen 1 und 3 ein.")
        chooseFirstPykemon(me)


def mainMenu(listOfOptions ):
    number = 1
    print(">>>>>>>>> Hauptmenü <<<<<<<<<")
    print("Was willst du tun")
    for option in listOfOptions:
        print(f"  {number} {option}")

        number += 1
    return input(" >")



intro()
while gameLoop:
    mainMenu()
