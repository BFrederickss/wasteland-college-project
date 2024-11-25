"""
file for the wasteland level

Author: Konrad Malara

Date started: 22/11/2024

Updates:
22/11/2024: getting the bases of the character class done, trying to do NPC too
            and the player class. Added a clock tick function that will decay the hunger
            and thirst bar over time. Most of the survival mechanic is done.

25/11/2024: Added a more important character class, helpers, that will help the player
            get through the level. Made a separate file to make the game work. Added a world
            class that will show the player where they are and where they can go. Added a quest
            mechanic that will help the player get through the level. Added a clue mechanic that
            will help the player get through the level.

to do:
survival mechanic(DONE): player has to survive in this land by trying to find water and food

clues(add more clues): getting the clues or set pieces so the portal activates and the player
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
# they will help the player get through the level
class helper(characters):
    def __init__(self, name, dialogue):
        super(helper, self).__init__(name, dialogue)
        self._name = "dimitri"

    def __repr__(self):
        return f"{self._name} {self._dialogue}"

    def provide_clue(self):
        clue = "You should go to the old church, there might be something there that will help you"
        print(clue)
        player.add_clue(clue)
        player.add_quest("Go to the old church, find gold Belarusian coin")
        print("If you want another clue, comeback with a golden Belarusian coin. you can go away now...")


class player:
    def __init__(self, name):
        self.hungerBar = 10
        self.thirstBar = 10
        self.healthBar = 20
        self._name = name
        self.space = []
        self.__clues = []
        self.quest = []
        self._location = "Abandoned house"

    # Inventory mechanic, not final
    def check_if_full(self):
        if len(self.space) > 10:
            print("You're invetory is full")

    # Views the inventory
    def view_invetory(self):
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
    def call_clock_tick(self):
        while True:
            self.__clock_tick()
            time.sleep(300)

    # I dont think this is final
    def death(self):
        while True:
            if self.hungerBar == 0:
                self.healthBar =-2

            if self.thirstBar == 0:
                self.healthBar =-1

            if self.healthBar == 0:
                print("You have died")
                break

    def add_item(self):
        ans = input("Would you like to add this item to the inventory? y/n: ")

        while ans == 'y' or ans == 'n':
            if ans == 'y':
                self.space.append()
            elif ans == 'n':
                print("Item discarded")
            else:
                print("Wrong answer try again")


    def review_clues(self):
        if len(self.__clues) > 0:
            for i in self.__clues:
                print(i)
        else:
            print("You have no clues yet")

    def add_clue(self,clue):
        self.__clues.append(clue)

    def add_quest(self, quest):
        self.quest.append(quest)

    def view_quest(self):
        for i in self.quest:
            print(i)

# world class that will show the player where they are and where they can go
# the player will have to find clues to get to the next level
# the player will have to find food and water to survive
# the player will have to find items to help them get through the level(this might be implemented)
class world:
    def __init__(self):
        self._world = ["Old church", "Abandoned house", "Quiet farm", "Old nuclear reactor", "Old rotten school"]
        self._player_location = "Abandoned house"

    def view_world(self):
        print("You are currently in: ", self._player_location)
        for i in self._world:
            print(i)

# locations in the world
# each location will have items and clues that the player can find
# ALL ITEMS IN THE WORLDS ARE NOT FINAL!!!!!
class abandoned_house(world):
    def __init__(self):
        super(abandoned_house,self).__init__()
        self._items = ["Old rusty knife", "Empty bottle", "Old piece of bread", "Old rotten apple"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Abandoned house"


class old_church(world):
    def __init__(self):
        super(old_church, self).__init__()
        self._items = ["Old cross", "Old bible", "Old candle", "Old chalice"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old church"

class quiet_farm(world):
    def __init__(self):
        super(quiet_farm, self).__init__()
        self._items = ["Old rusty pitchfork", "Old hoe", "Old shovel", "Old rake"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Quiet farm"

class old_nuclear_reactor(world):
    def __init__(self):
        super(old_nuclear_reactor, self).__init__()
        self._items = ["Old uranium rod", "Old nuclear reactor manual", "Old nuclear reactor key", "Old nuclear reactor button"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old nuclear reactor"

class old_rotten_school(world):
    def __init__(self):
        super(old_rotten_school, self).__init__()
        self._items = ["Old rusty scissors", "Old chalk", "Old ruler", "Old pen"]
        self._clues = ["Old map", "Old journal", "Old photo", "Old letter"]
        self._location = "Old rotten school"















