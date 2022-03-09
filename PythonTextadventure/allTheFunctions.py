def nextStep():
    nextStep = True
    while nextStep:
        answer = input("Was willst du dagegen machen?\nKämpfen(1)\nItems(2)\nFlüchten(3)")
        if answer == "1":
            print("ja wirklich")
            nextStep = False