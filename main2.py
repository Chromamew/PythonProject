
field = ["",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

def print_field():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])


def next_move():

    while True:
        player_move = input("Bitte das gewünschte Feld eingeben")
        if int(player_move) >= 1 and int(player_move) <= 9:
            return player_move
        else:
            print("Die eingegebene Zahl muss zwischen 1-9 liegen. Bitte wiederholen")


print((next_move()))