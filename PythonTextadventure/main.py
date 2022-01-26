import allTheMonster
import conversations
import player


me = player.Player("", 200, 200,  [], 0, 0, 0,)
me.name = input(conversations.how_am_i)
print(f"Hallo {me.name}")
conversations.intro

while True:
    print(conversations.mainMenu)
    q = input(conversations.Q_mainMenu)
    if q == "1":
        print("Du hast 1 eingegeben\n")
    elif q == "2":
        print("Du hast 2 gedrückt\n")
    elif q == "3":
        print("Du hast 3 gedrückt\n")
    elif q == "4":
        print("Du hast 4 gedrückt\n")
    else:
        print("Bitte eine richtige Eingabe machen")