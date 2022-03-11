players = []

class Player:
    def __init__(self, name):
        self.name = name
        self.point = 0

def create_players():
    p = int(input("Enter the number of player: "))
    for i in range(1,p+1):
        player = input(f"Enter the name of player no.{i} : ")
        players.append(Player(player))

