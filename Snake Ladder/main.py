import random
import time
from player import *
from ladder import Ladder
from snake import Snake

print("Welcome to Snake Ladder Game!")

snakes = Snake()
snakes.create_snake()

ladders = Ladder()
ladders.create_ladder()

create_players()


def dice_rolling():
    print("Dice rolling ...!")
    time.sleep(2)
    dice = random.randint(1,6)
    print(f"Dice showed {dice}")
    return dice

game_is_on = True

def play():
    global game_is_on

    for name in players:
        time.sleep(1)
        print(f"Your turn, {name.name}.")
        time.sleep(0.5)
        choice = input("Type 1 to continue, type 0 to pass or type q to quit the game: ")

        if choice == "1":        
            dice = dice_rolling()

            if (name.point + dice) > 100:
                print(f"Position can't move as it'll be bigger than 100")
            else:
                name.point += dice
                name.point = ladders.checkLadder(name.point)
                name.point = snakes.check_snake(name.point)
                print(f"Your position moved to {name.point}")

            if name.point == 100:
                time.sleep(1)
                print(f"Yay ! You won {name.name}.")
                game_is_on = False
                break
                
                
        elif choice == "0":
            pass

        else:
            print("Goodbye !")
            game_is_on = False
            break
            

while game_is_on:
    play()

