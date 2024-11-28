"""
file for the wasteland level

Author: Konrad Malara

Date started: 25/11/2024

Updates:
25/11/2024: This file was created as the base of the game is needed to be done. The game will be a text based adventure
            game that will have a few levels. The player will have to survive in the wasteland and find clues to get to the
            next level. The game will have a few(or maybe just 1) NPCs that will help the player get through the level.
            The player will have to find food and water to survive.

26/11/2024: Finally decided to check if my files even work and run, they do. Finished abandoned_house file, wasteland file
            had its own issues with the player class, such as player add item but that was fixed. Made it so the player
            can explore the house and get items and clues. Made it so the player can check their inventory and status.
            The player can also go back to menu and quit the game. The game is somewhat playable now with only one level.

to do:

- make the game somewhat playable
- make the wolrd class workable



"""

from wasteland import *
from world.world import world as wd
from world.abandoned_house import abandoned_house as ah
from world.quiet_farm import quiet_farm as qf

# game class that will run the game
# its here for now, as of 25th November, will not do a lot of things to it
# right now, but will add more to it as the game progresses.
class Game:
    def __init__(self):
        self._player = Player("Player")

        self._wd = wd()
        self._ah = ah()
        self._helpers = [Helper1("Xavier", "I can help you get through this level")]
        self._qf = qf()
        self.levels = self._wd._levels



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
            print("2. explore the house")
            print("3. Check your status")
            print("4. Check inventory")
            print("5. Quit")
            print("")

            choice = input("Enter your choice: ")

            if choice == "1":
                for i in self._wd._levels[i]:
                    print(i)
                print("Where do you want to go?")
                decide = int(input())
                while True:
                    if decide == 1:
                        print("Going to the abandoned house")
                        self._ah.explore_house()
                        break
                    elif decide == 2:
                        print("Going to the quiet farm")
                        self._qf.explore_farm()
                        break
                    else:
                        print("Invalid choice")
                        print("Where do you want to go?")
                        decide = int(input())

                if self._player.hungerBar < 5:
                    print("You feel hungry")
                if self._player.thirstBar < 5:
                    print("You feel thirsty")
                print("")

            elif choice == "2":
                print("You look around and see the house")
                self._ah.explore_house()
                print("")

            elif choice == "3":
                print(f"Your hunger: {self._player.hungerBar}")
                print(f"Your thirst: {self._player.thirstBar}")
                print(f"Your health: {self._player.healthBar}")
                print("")

            elif choice == "4":
                self._player.view_invetory()
                print("")

            elif choice == "5":
                print("Goodbye")
                break

            else:
                print("Invalid choice")
                print("")

# run the game
if __name__ == "__main__":
    game = Game()
    game.start()