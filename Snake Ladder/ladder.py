class Ladder:
    def __init__(self):
        self.ladderPosition = {}

    def checkLadder(self, point):
        if (point in self.ladderPosition.keys()):
            print("climbing up!!")
            return self.ladderPosition[point]
        else:
            return point

    def create_ladder(self):
        l = int(input("Enter the number of ladders: "))
        for i in range(1,l+1):
            temp = list(map(int, input(f"Enter start and end position of ladder no.{i} : ").split()))
            self.ladderPosition[temp[0]] = temp[1]