"""
file for the wasteland level

Author: Konrad Malara

Date started: 22/11/2024

Updates:
22/11/2024 getting the bases of the character class done, trying to do NPC too
           and the player class

to do:
survival mechanic, player has to survive in this land by trying to find water and food
clues, getting the clues or set pieces so the portal activates and the player
       can teleport to the next level

"""

from abc import ABC, abstractmethod
import random as rnd
import time



class characters:

    def __init__(self,name, dialogue):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False


    def interaction(self):
        if not self._interacted:
            interaction = f"{self._name}: f{self._dialogue}"
        else:
            interaction = f"{self._name}: no longer interested in talking to you"

        return interaction


class NPC(characters):
    def __init__(self, dialogue):
        super(NPC, self).__init__()
        self._dialogue = dialogue

    def __repr__(self):
        return f"{self._name} {self._dialogue}"

    def randomDialogue(self):
        talkList = ["Why are you here? Don't you see its dangerous?", "You're better off running "
                    "away from this acursed land", "You're waste of space", "AHRGGGGGGGHHHHHH"]

        decide = rnd.randint(1, len(talkList))

        dialogue =  talkList[decide]

# more important characters
#class

class player:
    def __init__(self, name):
        self.hungerBar = 10
        self.thirstBar = 10
        self.healthBar = 20
        self._name = name
        self.space = []

    # Inventory mechanic, not final
    def checkiffull(self):
        if len(self.space) > 10:
            print("You're invetory is full")

    # Views the inventory
    def viewinvetory(self):
        for i in self.space:
            print(self.space[i])

    # Hunger bar and thirst bar decay over time so the player is forced
    # to explore the world a lot more and to find food/water for survival
    def __clock_tick(self):
        self.hungerBar -= 1
        self.thirstBar -= 1

        print("Hunger: ",self.hungerBar,"Thirst: ", self.thirstBar)
        if self.hungerBar < 5:
            print("You are getting pretty hungry, you should eat or find some food")

        if self.thirstBar < 5:
            print("You are getting pretty thirsty, you should find water or drink something")

    # Calls back clock tick so the hunger bar and thirst bar can get low
    # over time
    def callClockTick(self):
        while True:
            self.__clock_tick()
            time.sleep(300)

    # I dont think this is final
    def death(self):
        while True:
            if self.hungerBar == 0:
                self.healthBar =-2

            if self.thirstBar == 0:
                self.healthBar == -1

    def additem(self):
        ans = input("Would you like to add this item to the inventory? y/n: ")

        while ans == 'y' or ans == 'n':
            if ans == 'y':
                self.space.append()
            elif ans == 'n':
                print("Item discarded")
            else:
                print("Wrong answer try again")









"""
class evilPeople(characters):
"""







