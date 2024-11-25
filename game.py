"""
file for the wasteland level

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: This file was created as the base of the game is needed to be done. The game will be a text based adventure
            game that will have a few levels. The player will have to survive in the wasteland and find clues to get to the
            next level. The game will have a few(or maybe just 1) NPCs that will help the player get through the level.
            The player will have to find food and water to survive.


to do:

- make the game somewhat playable
- make the wolrd class workable



"""

from wasteland import *
from world.world import world


# game class that will run the game
# its here for now, as of 25th November, will not do a lot of things to it
# right now, but will add more to it as the game progresses.
class Game:
    def __init__(self):
        self._player = Player()
        self._world = world()
        self._helpers = [Helper("Xavier")]
        self._npc = NPC("You're better off running away from this acursed land")

    def start(self):
        print("Welcome to the wasteland"
              "You have been teleported to this land by a mysterious force")
        print("You have to survive in this land by finding food and water")
        print("You also have to find clues to get to the next level")
        print("Good luck")
        print("")

        while True:

            print("What do you want to do?")
            print("1. Look at the map")
            print("2. Talk to someone")
            print("3. Check your status")
            print("4. Quit")
            print("")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("You look around and see rotten walls and fungus around the room")
                if self._player.hungerBar < 5:
                    print("You feel hungry")
                if self._player.thirstBar < 5:
                    print("You feel thirsty")
                print("")

            elif choice == "2":
                print(self._npc.interaction())
                print("")

            elif choice == "3":
                print(self._player)
                print("")

            elif choice == "4":
                print("Goodbye")
                break

            else:
                print("Invalid choice")
                print("")