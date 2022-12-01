import player
import allPokemon
import random

gameloop = True
me = player.Player([], [], [], [], "", 0, [])


def intro(me):
    me.name = input("Btte gib Deinen Namen ein!\n ")
    print(f"Willkommen in der Welt von POKEMON {me.name}, schön das du bei uns bist!\nSicher weisst du Bescheid, "
          f"dass du von mir, Dr:Acor, dein allererstes POKEMON bekommst.\nDir stehen folgende POKEMON zur "
          f"Auswahl:\n1: Bisasam\n2: Gluamanda\n3: Schiggy")
    while True:
        userInput = input("Bitte wähle mit Bedacht.\n")
        if userInput == "1" or userInput == "bisasam":
            me.pokemon.append(allPokemon.allpokemon["PflanzenPokemon"][0])
            print(
                f"Sehr schön, Du hast dich für {me.pokemon[0].name} entscheiden. Ein hervorragendes Pflanzen POKEMON!")
            giveNameToPokemon(me)
            break
        elif userInput == "2" or userInput == "glumanda":
            me.pokemon.append(allPokemon.allpokemon["FeuerPokemon"][0])
            print(f"Hervorragend, {me.pokemon[0].name} ist ein beeindruckendes Feuer POKEMON!")
            giveNameToPokemon(me)
            break
        elif userInput == "3" or userInput == "shiggy".lower():
            me.pokemon.append(allPokemon.allpokemon["WasserPokemon"][0])
            print(f"{me.pokemon[0].name} also! Eine sehr gute Wahl mit einem Wasser POKEMON zu starten!")
            giveNameToPokemon(me)
            break
    return me


def calcPokemonStats(randomokemon, level):
    randomokemon.level = level


def searchEncounterPokemon():
    randomPokemon = random.choice(allPokemon.allpokemon[random.choice(
        ["WasserPokemon", "FeuerPokemon", "PflanzenPokemon", "NormalePokemon", "KäferPokemon", "ElektroPokemon"])])
    level = random.randint(1, 10)
    calcPokemonStats(randomPokemon, level)
    if randomPokemon.level >= 10:
        print(f"Das Pokemon {randomPokemon.name} ({randomPokemon.level}) ist zu hohes level")
        return randomPokemon
    else:
        print(f"Ein wildes {randomPokemon.name} Level {randomPokemon.level} greift Dich an.")
        return randomPokemon


def levelUp(pokemon):
    pokemon.level += 1
    return pokemon


def sendPokemonToFight():
    print(f"Du schickst {me.pokemon[0].name} Level {me.pokemon[0].level} in den Kampf")


# ein komentr der den ich erstelle what ever
def chooseYourAttack(pokemon):
    tempNum = 1
    print("Wähle eine Atacke\n")
    for attack in pokemon.attackList:
        print(f"{tempNum}:{attack.name}")
        tempNum += 1
    userinput = input("Bitte Wählen\n")
    if userinput == "1":
        return pokemon.attackList[0]
    elif userinput == "2":
        return pokemon.attackList[1]

def chooseEncounterAttack(encounterPokemon):
   return random.choice(encounterPokemon.attackList)

def calcDmg(myPokemon, encounterEnemy, yourAttack, encounterAttack):
    encounterEnemy.currentHp -= yourAttack.baseDmg
    print(f"{myPokemon.name} hat {encounterEnemy.name} mit {yourAttack.name} {yourAttack.baseDmg} Schaden zugefügt")

    myPokemon.currentHp -= encounterAttack.baseDmg
    print(f"{encounterEnemy.name} hat deinem {myPokemon.name} mit {encounterAttack.name} {encounterAttack.baseDmg} Schaden zugefügt\n")




def selectPokemonAttack(userinput):
    pass

# a beide suchen sich ihre attacken  FERTIG
# b dann wird geschaut wer zuerst angreift(erstmal übersprungen)
# c dann wird der schaden berechent.
# d fertig
def fight(encounterPokemon, me):
    yourAttack = chooseYourAttack(me.pokemon[0])
    encounterAttack = chooseEncounterAttack(encounterPokemon)
    calcDmg(me.pokemon[0], encounterPokemon, yourAttack, encounterAttack)

    if me.pokemon[0].currentHp <= 0:
        print("Dein pokemon ist besiegt")
        return False
    elif encounterPokemon.currentHp <= 0:
        print(f"{encounterPokemon.name} wurde besiegt")
        return False
    return True

def notAvailable():
    print("Leider noch nciht verfügbar\n...")


def showItems():
    notAvailable()


def changeFrontPokemon():
    notAvailable()


def changeRegion():
    notAvailable()


def giveNameToPokemon(me):
    userInput = input("Möchtest du deinem POKEMON einen neuen Namen geben?\n")
    if userInput == "ja".lower():
        current_name = me.pokemon[0].name
        userInput = input("Wie soll der neue Name lauten?\n")
        me.pokemon[0].alias = userInput
        print(f"Sehr schön, dein POKEMON höer jetzt auf den Namen '{me.pokemon[0].alias}'")
    else:
        me.pokemon[0].alias = me.pokemon[0].name
        print(f"Gut... dann nicht. Es hört weiterhin auf den Namen '{me.pokemon[0].alias}'")
        return


def encounterMenue(enounterPokemon, me):
    sendPokemonToFight()
    #userinput = input("Was willst du machen?\n1: Kämpfen\n2: Pokemon wechseln\n3: Items\n4: fliehen\n")
    infight = True
    while infight:
        userinput = input("Was willst du machen?\n1: Kämpfen\n2: Pokemon wechseln\n3: Items\n4: fliehen\n")
        if userinput == "1":
            infight = fight(enounterPokemon, me)

        elif userinput == "2":
            changeFrontPokemon()

        elif userinput == "3":
            showItems()

        elif userinput == "4":
            print("Du bist entkommen")
            me.pokemonEncounter = []
            break


# Hauptmenü zum Navigieren
def mainMenu(me):
    print("\n*****Hauptmenü*****\n\n"
          "1: Suche nach Wilden Pokemon\n"
          "2: Zeige meine POKEMON\n"
          "3: Items\n"
          "4: Wechsel Region\n")
    userInput = input("Was möchstest du machen?\n")

    if userInput == "1":
        enounterPokemon = searchEncounterPokemon()
        encounterMenue(enounterPokemon, me)
    elif userInput == "2":
        tempNum = 1
        print("Derzeit führst du folgene POKEMON mit dir: ")
        for pokemon in me.pokemon:
            if(pokemon.alias == pokemon.name):
                print(f"{tempNum} {pokemon.alias}")
            else:
                print(f"{tempNum} {pokemon.alias} ({pokemon.name})")
            tempNum += 1
    elif userInput == "3":
        for item in me.items:
            print(item)
    elif userInput == "4":
        changeRegion()


intro(me)
while gameloop:
    mainMenu(me)
