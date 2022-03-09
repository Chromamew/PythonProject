import conversations
import movement as m
import player


me = player.Player("", 200, 200,  [], 0, 0, 0,)
me.name = input(conversations.how_am_i)
print(f"Hallo {me.name}")
conversations.intro

while True:
    print(conversations.mainMenu)
    q = input(conversations.Q_mainMenu)
    if q == "1":
        m.forward()
    elif q == "2":
        m.right()
    elif q == "3":
        m.backwards()
    elif q == "4":
        m.left()
    else:
        print("Bitte eine richtige Eingabe machen")