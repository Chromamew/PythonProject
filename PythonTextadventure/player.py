from operator import inv
from tokenize import maybe
from turtle import right


class Player():
    def __init__(self, name, currentHp, maxHp, inventar, rightHand, leftHand, armor):
        self.name = name
        self.currentHp = currentHp
        self.maxHp = maxHp
        self.inventar = inventar
        self.rightHand = rightHand
        self.leftHand = leftHand
        self.armor = armor


        