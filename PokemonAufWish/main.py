import re
import player
import allPokemon
import random
gameloop = True
me = player.Player([], [], [], [], "", 0, [])


def intro(me):
    me.name = input("Btte gib Deinen Namen ein! ")
    print(f"Willkommen in der Welt von POKEMON {me.name}, schön das du bei uns bist!\nSicher weisst du Bescheid, "
          f"dass du von mir, Dr:Acor, dein aller erstes POKEMON bekommst.\nDir stehen folgende POKEMON zur "
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

def searchWildPokemon():
    randomPokemon = random.choice(allPokemon.allpokemon[random.choice(["WasserPokemon", "FeuerPokemon", "PflanzenPokemon", "NormalePokemon", "KäferPokemon", "ElektroPokemon"])])
    level = random.randint(1, 10)
    calcPokemonStats(randomPokemon, level)
    if randomPokemon.level >= 10:
        print(f"Das Pokemon {randomPokemon.name} ist zu hohes level")
        return randomPokemon
    else:
        return randomPokemon

def levelUp(pokemon):
    pokemon.level += 1
    return pokemon

def kämpfen(Gegner, me):
    print(f"Du schickst {me.pokemon[0].name} Level {me.pokemon[0].level} in den Kampf")
    userInput = input("Wähle eine Atacke")
    for attack in me.pokemon[0].attackList:
        print(attack)


def changeRegion():
    input("Leider noch nicht verfügbar\n...")


def giveNameToPokemon(me):
    userInput = input("Möchtest du deinem POKEMON einen neuen Namen geben?\n")
    if userInput == "ja".lower():
        current_name = me.pokemon[0].name
        userInput = input("Wie soll der neue Name lauten?\n")
        me.pokemon[0].name = userInput
        print(f"Sehr schön, dein POKEMON höer jetzt auf den Namen '{me.pokemon[0].name}'")
    else:
        print(f"Gut... dann nicht. Es hört weiterhin auf den Namen '{me.pokemon[0].name}'")
        return

def searchEncounter():
    me.pokemonEncounter.append(searchWildPokemon())
    #print(me.pokemonEncounter[0].name)
    print(f"Du begegnest einem {me.pokemonEncounter[0].name} level {me.pokemonEncounter[0].level}")
    while True:
        userInput = input("****Kampfmenü****\n1: Kämpfen\n2: Pokemon Wechseln\n3: Items\n4: Fliehen\n")
        if userInput == "1":
            print("Kämpfen gewählt")
            kämpfen(me.pokemonEncounter[0], me)
            
        elif userInput == "2":
            print("Pokemon Wechseln")
            
        elif userInput == "3":
            print("Items")
            
        elif userInput == "4":
            print("Du fliehst")
            break
        else:
            print("Bitte passende Antwort geben")



def mainMenu(me):
    print("\n*****Hauptmenü*****\n\n"
          "1: Suche nach Wilden Pokemon\n"
          "2: Zeige meine POKEMON\n"
          "3: Items\n"
          "4: Wechsel Region\n")
    userInput = input("Was möchstest du machen?\n")
    if userInput == "1":
        searchEncounter()
    elif userInput == "2":
        for pokemon in me.pokemon:
            print(pokemon.name)
    elif userInput == "3":
        for item in me.items:
            print(item)
    elif userInput == "4":
        changeRegion()



intro(me)
while gameloop:
    mainMenu(me)

    # gameloop = False
