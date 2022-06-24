import random
import pokemon as pkm

allpokemon = {
    "WasserPokemon": [
        pkm.Pokemon(7, "Shiggy", 1, "WASSER", 50, 50, 0, 100, [], []),
        pkm.Pokemon(8, "Shillock", 16, "WASSER", 500, 500, 0, 1600, [], []),
        pkm.Pokemon(9, "Turtok", 36, "WASSER", 1200, 1200, 0, 5000, [], []),
    ],
    "FeuerPokemon": [
        pkm.Pokemon(4, "Glumanda", 1, "FEUER", 50, 50, 0, 100, [], []),
        pkm.Pokemon(5, "Glutexo", 16, "FEUER", 500, 500, 0, 1600, [], []),
        pkm.Pokemon(6, "Glurak", 36, "FEUER", 1200, 1200, 0, 5000, [], [])
    ],
    "PflanzenPokemon": [
        pkm.Pokemon(1, "Bisasam", 1, "PFLANZE", 50, 50, 0, 100, [], []),
        pkm.Pokemon(2, "Bisaknosp", "PFLANZE", 16, 500, 500, 0, 1600, [], []),
        pkm.Pokemon(3, "Bisalor", 36, "PFLANZE", 1200, 1200, 0, 5000, [], [])
    ]
}

def getAStarterPokemon():
    return allpokemon[random.choice(["WasserPokemon", "FeuerPokemon", "PflanzenPokemon"])]

