import player
import allPokemon


def intro(me):
    me.name = input("Btte gib Deinen Namen ein! ")
    print(f"Willkommen in der Welt von POKEMON {me.name}, schön das du bei uns bist!\nSicher weisst du Bescheid, "
          f"dass du von mir, Dr:Acer, dein aller erstes POKEMON bekommst.\nDir stehen folgende POKEMON zur "
          f"Auswahl:\n1: Bisasam\n2: Gluamanda\n3: Schiggy")
    while True:
        userInput = input("Bitte wähle nach Bedacht.\n")
        if userInput == "1" or userInput == "bisasam":
            me.pokemon.append(allPokemon.allpokemon["PflanzenPokemon"][0])
            print(f"Sehr schön, Du hast dich für {me.pokemon[0].name} entscheiden. Ein hervorragendes Pflanzen POKEMON!")
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

def giveNameToPokemon(me):
    userInput = input("Möchtest du deinem POKEMON einen neuen Namen geben?\n")
    if userInput == "ja".lower():
        current_name = me.pokemon[0].name
        userInput = input("Wie soll der neue Name lauten?\n")
        me.pokemon[0].name = userInput
        print(f"Sehr schön, dein POKEMON höer jetzt auf den Namen '{me.pokemon[0].name}'")
    else:
        print(f"Gut... dann nicht hört es weiterhin auf den Namen '{me.pokemon[0].name}'")
        return


def mainMenu(me):
    print("\n*****Hauptmenü*****\n\n"
          "1: Suche nach Wilden Pokemon\n"
          "2: Zeige meine POKEMON\n"
          "3: Items\n"
          "4: Wechsel Region\n")
    userInput = input("Was möchstest du machen?\n")
    if userInput == "1":
        pass
        searchWildPokemon()
    elif userInput == "2":
        for pokemon in me.pokemon:
            print(pokemon.name)
    elif userInput == "3":
        for item in me.items:
            print(item)
    elif userInput == "4":
        changeRegion()

def searchWildPokemon():
    print("Leider noc nicht verfügbar")

def changeRegion():
    print("Leider noc nicht verfügbar")


gameloop = True
while gameloop:
    me = player.Player([], [], [], "", 0, [])
    intro(me)
    mainMenu(me)


    gameloop = False

