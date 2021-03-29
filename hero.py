import random
import time

class Hero:
    def __init__(self, moves, health):

        self.moves = moves
        self.health = health

    def getMoves(self):
        return self.moves

    def getHealth(self):
        return self.health

    def loseHealth(self):
        self.health = self.health - 1



class Enemy:
    def __init__(self, health, uniqueAttack, name):
        self.health = health
        self.uniqueAttack = uniqueAttack
        self.name = name

def play():
    print("Hey Broc!!!!!!!!!")

play()