import random
from datetime import datetime

CHAR_CLOSED = '.'
CHAR_BOMB = '*'
CHAR_EMPTY = '_'

STATUS_IDLE = 0
STATUS_WINNING = 1
STATUS_LOSING = 2


class Minesweeper(object):

  def __init__(self, n, b):
    self.n = n
    self.b = b
    self.board = []
    self.opened = []
    self.bombCoordinates = []

    for _ in range(n):
      self.board.append([CHAR_EMPTY] * n)
      self.opened.append([False] * n)

    # generate bombs in the board
    random.seed(datetime.now())
    remainingBombs = self.b
    while remainingBombs > 0:
      x, y = random.randint(0, self.n-1), random.randint(0, self.n-1)
      if self.board[x][y] != CHAR_BOMB:
        self.board[x][y] = CHAR_BOMB
        self.bombCoordinates.append((x,y))
        remainingBombs -= 1

    # all complete: bombs are set
    # the next step is to insert number indicators
    self.setNumberIndicators()

  def setNumberIndicators(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if not self.isBomb(i, j):
          count = self.countSurroundingBombs(i, j)
          if count > 0:
            self.board[i][j] = str(count)

  def countSurroundingBombs(self, x, y):
    counter = 0
    for i in range(x - 1, x + 2):
      for j in range(y - 1, y + 2):
        if (0 <= i < self.n) and (0 <= j < self.n) and (x != i or y != j) and self.isBomb(i, j):
          counter += 1

    return counter

  def printBoard(self):
    print()

    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if self.opened[i][j]:
          print(self.board[i][j], end=' ')
        else:
          print(CHAR_CLOSED, end=' ')

      print()
    print()

  def openAllBombs(self):
    for p in self.bombCoordinates:
      self.opened[p[0]][p[1]] = True

  def checkClickedPoint(self, x, y):
    if not self.opened[x][y]:
      if self.isBomb(x, y):
        self.openAllBombs()
        return False
      else:
        self.open(x, y)
        return True

    return True

  def isBomb(self, x, y):
    return self.board[x][y] == CHAR_BOMB

  def open(self, x, y):
    if 0 <= x < self.n and 0 <= y < self.n:
      if not self.opened[x][y]:
        self.opened[x][y] = True

        if self.board[x][y] == CHAR_EMPTY:
          self.open(x-1, y-1)
          self.open(x-1, y)
          self.open(x-1, y+1)
          self.open(x, y-1)
          self.open(x, y+1)
          self.open(x+1, y-1)
          self.open(x+1, y)
          self.open(x+1, y+1)

  def isGameFinished(self):
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        if not self.opened[i][j] and not self.isBomb(i, j):
          return False

    return True

  def validPoint(self, x, y):
    return 0 <= x < self.n and 0 <= y < self.n

  def start(self):
    status = STATUS_IDLE

    while status == STATUS_IDLE:
      self.printBoard()
      y, x = map(int, input("Enter a coordinate point (x y): ").split())

      if self.validPoint(x, y):
        if self.checkClickedPoint(x, y):
          if self.isGameFinished():
            status = STATUS_WINNING
        else:
          status = STATUS_LOSING
          print("BOOM! You lose!")
      else:
        print("Oops! x and y value must be between 0 and %d" % (self.n - 1))

    self.printBoard()


def main():
  print("Welcome to Minesweeper CLI!")
  n = int(input("Please enter the square size: "))
  b = int(input("Please enter the number of mines: "))

  game = Minesweeper(n, b)
  game.start()


if __name__ == '__main__':
  main()
