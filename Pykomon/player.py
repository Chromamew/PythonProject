class Player:
    def __init__(self, name):
        self.name = name
        self.pykedex = []
        self.currentFrontPykemon = None
        self.pykemonList = []
        self.currentWallet = 0
        self.currentBatches = []

    def saveGame(self):
        pass

    def showCurrentWallet(self):
        return self.currentWallet

    def showCurrentFrontPykemon(self):
        return self.currentFrontPykemon

    def showPykedex(self):
        for pykmon in self.pykedex:
            print(pykmon.name)
        return self.pykedex
    def showCurrentBatches(self):
        return self.currentBatches
