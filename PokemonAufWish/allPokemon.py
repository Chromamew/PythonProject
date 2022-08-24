import random
import pokemon as pkm
import allPokemonAttacks 

allpokemon = {
    "WasserPokemon": [
        pkm.Pokemon(7, "Shiggy", 1, "WASSER", 50, 50, 0, 100, [ allPokemonAttacks.tacke,allPokemonAttacks.bite], []),
        pkm.Pokemon(8, "Shillock", 1, "WASSER", 500, 500, 0, 1600, [], []),
        pkm.Pokemon(9, "Turtok", 1, "WASSER", 1200, 1200, 0, 5000, [], []),
    ],
    "FeuerPokemon": [
        pkm.Pokemon(4, "Glumanda", 1, "FEUER", 50, 50, 0, 100, [], []),
        pkm.Pokemon(5, "Glutexo", 1, "FEUER", 500, 500, 0, 1600, [], []),
        pkm.Pokemon(6, "Glurak", 1, "FEUER", 1200, 1200, 0, 5000, [], [])
    ],
    "PflanzenPokemon": [
        pkm.Pokemon(1, "Bisasam", 1, "PFLANZE", 50, 50, 0, 100, [], []),
        pkm.Pokemon(2, "Bisaknosp", 1, "PFLANZE", 500, 500, 0, 1600, [], []),
        pkm.Pokemon(3, "Bisalor", 1, "PFLANZE", 1200, 1200, 0, 5000, [], [])
    ],
    "KäferPokemon": [
        pkm.Pokemon(10, "Raupi", 1, "Käfer", 35, 35, 0, 80, [], []),
        pkm.Pokemon(11, "Safcon", 1, "Käfer", 500, 500, 0, 1500, [], []),
        pkm.Pokemon(12, "Smettbo", 1, "Käfer", 1000, 1000, 0, 4000, [], []),
        pkm.Pokemon(13, "Hornliu", 1, "Käfer", 35, 35, 0, 80, [], []),
        pkm.Pokemon(14, "Kokuna", 1, "Käfer", 500, 500, 0, 1500, [], []),
        pkm.Pokemon(15, "Bibor", 1, "Käfer", 1000, 1000, 0, 4000, [], []),
    ],
    "NormalePokemon": [
        pkm.Pokemon(16, "Taubsi", 1, "Normal", 50, 50, 0, 100, [], []),
        pkm.Pokemon(17, "Tauboga", 1, "Normal", 500, 50, 0, 1600, [], []),
        pkm.Pokemon(18, "Tauboss", 1, "Normal", 1200, 1200, 0, 5000, [], []),
        pkm.Pokemon(19, "Rattfratz", 1, "Normal", 45, 45, 0, 90, [], []),
        pkm.Pokemon(20, "Rattikarl", 1, "Normal", 1100, 1100, 0, 4200, [], []),
        pkm.Pokemon(21, "Habitak", 1, "Normal", 50, 50, 0, 100, [], []),
        pkm.Pokemon(22, "Ibitak", 1, "Normal", 1100, 1100, 0, 4200, [], []),
    ],
    "GiftPokemon": [
        pkm.Pokemon(23, "Rettern", 1, "Gift", 35, 35, 0, 100, [], []),
        pkm.Pokemon(24, "Arbok", 1, "Gift", 400, 400, 0, 4000, [], []),
        pkm.Pokemon

    ],
    "ElektroPokemon": [
        pkm.Pokemon(25, "Pikatchu", 1, "Elektro", 40, 40, 0, 100, [], []),
        pkm.Pokemon(26, "Reichu", 1, "Elektro", 500, 500, 0, 5000, [], [])
    ]
}


def getAStarterPokemon():
    return allpokemon[random.choice(["WasserPokemon", "FeuerPokemon", "PflanzenPokemon"])]




