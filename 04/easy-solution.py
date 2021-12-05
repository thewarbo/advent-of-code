import os

class BingoBoard:
    def __init__(self, lines) -> None:
        self.board = []
        self.called = []
        for myRow in lines:
            self.board.append(myRow);
            self.called.append([False] * len(myRow))
    
    def call(self, number):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                   self.called[i][j] = True;
                   break
        return None
    
    def win(self):
        for i in range(5):
            if(all(self.called[i])):
                return True
        for j in range(5):
            if(all([self.called[i][j] for i in range(5)])):
                return True
        return False
    
    def score(self):
        value = 0
        for i in range(5):
            for j in range(5):
                if(not self.called[i][j]):
                    value += self.board[i][j]
        return value


lines = open(os.path.join(os.path.dirname(__file__),"input")).readlines()
numbers = [int(number) for number in lines[0].split(",")]

lines = lines[2:len(lines)]
boards = []
board = []
for line in lines:
    if line.strip() == "":
        boards.append(BingoBoard(board))
        board = []
    else:
        board.append( [int(number) for number in line.split()] )

done = False
for number in numbers:
    if done:
        break
    for board in boards:
        board.call(number)
    for board in boards:
        if board.win():
            print(board.score() * number)
            done = True