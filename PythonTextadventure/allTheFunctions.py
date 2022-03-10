def nextStep():
    nextStep = True
    while nextStep:
        answer = input("Was willst du dagegen machen?\nKämpfen(1)\nItems(2)\nFlüchten(3)")
        if answer == "1":
            print("Kämpfen gewählt")
            nextStep = False
        elif answer == "2":
            print("Items gewählt")
            nextStep = False
        elif answer == "3":
            print("Flüchten")
            nextStep = False
        else:
            print("Bitte Was!")