class Snake:
    def __init__(self):
        self.snakePosition = {}

    def check_snake(self, point):
        if (point in self.snakePosition.keys()):
            print("ouch! snake bite!!")
            return self.snakePostion[point]
        else:
            return point

    def create_snake(self):
        s = int(input("Enter the number of snakes: "))
        for i in range(1,s+1):
            temp = list(map(int, input(f"Enter head and tail position of snake no.{i} : ").split()))
            self.snakePosition[temp[0]] = temp[1]
