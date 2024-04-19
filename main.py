import os
import time
import copy
import random

from getkey import getkey, keys

class bcolors:
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'

X = f"{bcolors.FAIL}X{bcolors.ENDC}"
O = f"{bcolors.OKGREEN}O{bcolors.ENDC}"
tempX = f"{bcolors.OKBLUE}X{bcolors.ENDC}"
tempO = f"{bcolors.OKBLUE}O{bcolors.ENDC}"

class Game():
  def __init__(self):
    self.turn = ""

  def init(self):
    self.turn = random.choice([X, O])

  def switch_turn(self):
    if self.turn == X:
      self.turn = O
    else:
      self.turn = X

  def check_win(self, grid):
    if grid.a1 == X and grid.a2 == X and grid.a3 == X:
      return 1
    if grid.b1 == X and grid.b2 == X and grid.b3 == X:
      return 1
    if grid.c1 == X and grid.c2 == X and grid.c3 == X:
      return 1
    if grid.a1 == O and grid.a2 == O and grid.a3 == O:
      return 2
    if grid.b1 == O and grid.b2 == O and grid.b3 == O:
      return 2
    if grid.c1 == O and grid.c2 == O and grid.c3 == O:
      return 2

    if grid.a1 == X and grid.b1 == X and grid.c1 == X:
      return 1
    if grid.a2 == X and grid.b2 == X and grid.c2 == X:
      return 1
    if grid.a3 == X and grid.b3 == X and grid.c3 == X:
      return 1
    if grid.a1 == O and grid.b1 == O and grid.c1 == O:
      return 2
    if grid.a2 == O and grid.b2 == O and grid.c2 == O:
      return 2
    if grid.a3 == O and grid.b3 == O and grid.c3 == O:
      return 2

    if grid.a1 == X and grid.b2 == X and grid.c3 == X:
      return 1
    if grid.a3 == X and grid.b2 == X and grid.c1 == X:
      return 1
    if grid.a1 == O and grid.b2 == O and grid.c3 == O:
      return 2
    if grid.a3 == O and grid.b2 == O and grid.c1 == O:
      return 2

    return 0

class Grid():
  def __init__(self):
    self.a1 = " "
    self.a2 = " "
    self.a3 = " "
    
    self.b1 = " "
    self.b2 = " "
    self.b3 = " "
    
    self.c1 = " "
    self.c2 = " "
    self.c3 = " "

    self.row = "a"
    self.column = 1
  
  def output(self):
    print("+-----------+")
    print(f"| {self.a1} | {self.a2} | {self.a3} |")
    print("+-----------+")
    print(f"| {self.b1} | {self.b2} | {self.b3} |")
    print("+-----------+")
    print(f"| {self.c1} | {self.c2} | {self.c3} |")
    print("+-----------+\n")

  def reset(self, new):
    self.a1 = new.a1
    self.a2 = new.a2
    self.a3 = new.a3
    
    self.b1 = new.b1
    self.b2 = new.b2
    self.b3 = new.b3
    
    self.c1 = new.c1
    self.c2 = new.c2
    self.c3 = new.c3

  def free_spaces(self):
    spaces = []

    if self.a1 == " ":
      spaces.append("a1")
    if self.a2 == " ":
      spaces.append("a2")
    if self.a3 == " ":
      spaces.append("a3")
    if self.b1 == " ":
      spaces.append("b1")
    if self.b2 == " ":
      spaces.append("b2")
    if self.b3 == " ":
      spaces.append("b3")
    if self.c1 == " ":
      spaces.append("c1")
    if self.c2 == " ":
      spaces.append("c2")
    if self.c3 == " ":
      spaces.append("c3")
    
    return spaces

game = Game()
game.init()

saved_board = Grid()
temp_board = Grid()

if game.turn == O:
  temp_board.a1 = tempO

class Computer():
  def __init__(self):
    mark = "X"
  
  class Easy():
    def move(self):
      possible_moves = saved_board.free_spaces()
      move = 0
      has_won = ""
    
      for let in [X, O]:
        for i in possible_moves:
          board_copy = copy.deepcopy(saved_board)
          board_copy.__dict__[i] = let
    
          win_check = game.check_win(board_copy)
          
          if win_check != 0:
            move = i
    
            if win_check == 1:
              return move
    
            has_won = "O"
    
      if has_won != "":
        return move
    
      open_corners = []
      for i in possible_moves:
        if i in ["a1", "a3", "c1", "c3"]:
          open_corners.append(i)
    
      if len(open_corners) > 0:
        move = random.choice(open_corners)
        return move
    
      move = random.choice(possible_moves)
      return move
  
  class Hard():
    def move(self):
      possible_moves = saved_board.free_spaces()
      move = 0
      has_won = ""
      player_corners = 0
      player_edges = 0
    
      for let in [X, O]:
        for i in possible_moves:
          board_copy = copy.deepcopy(saved_board)
          board_copy.__dict__[i] = let
    
          win_check = game.check_win(board_copy)
          
          if win_check != 0:
            move = i
    
            if win_check == 1:
              return move
    
            has_won = "O"
    
      if has_won != "":
        return move

      if saved_board.__dict__["a1"] == O and saved_board.__dict__["b3"] == O and saved_board.__dict__["c2"] == O:
        return "c3"
      elif saved_board.__dict__["a3"] == O and saved_board.__dict__["b1"] == O and saved_board.__dict__["c2"] == O:
        return "c1"
      elif saved_board.__dict__["c1"] == O and saved_board.__dict__["a2"] == O and saved_board.__dict__["b3"] == O:
        return "a3"
      elif saved_board.__dict__["c3"] == O and saved_board.__dict__["a2"] == O and saved_board.__dict__["b1"] == O:
        return "a1"
      
      if "b2" in possible_moves:
        return "b2"
    
      open_corners = []
      for i in possible_moves:
        if i in ["a1", "a3", "c1", "c3"]:
          open_corners.append(i)

      open_edges = []
      for i in possible_moves:
        if i in ["a2", "c2", "b1", "b3"]:
          open_edges.append(i)

      if len(open_corners) >= 0:
        for i in open_corners:
          if saved_board.__dict__[i] != "X":
            player_corners += 1

      if len(open_edges) >= 0:
        for i in open_edges:
          if saved_board.__dict__[i] != "X":
            player_edges += 1

      if player_corners >= 2 or player_corners > 0 and player_edges > 0:
        if len(open_edges) > 0:
          move = random.choice(open_edges)
          return move
      
      if len(open_corners) > 0:
        move = random.choice(open_corners)
        return move
    
      move = random.choice(possible_moves)
      return move

os.system("clear")
print(f"Welcome to {bcolors.BOLD}Tic Tac Toe{bcolors.ENDC}!\n")
print(f"Would you like to start an {bcolors.BOLD}EASY{bcolors.ENDC} or {bcolors.BOLD}HARD{bcolors.ENDC} game?")
difficulty = input("\n(E / H) > ").lower()

while True:
  if difficulty == "e":
    computer_ai = Computer().Easy()
    break
  elif difficulty == "h":
    computer_ai = Computer().Hard()
    break
  else:
    os.system("clear")
    print(f"Welcome to {bcolors.BOLD}Tic Tac Toe{bcolors.ENDC}!\n")
    print(f"Would you like to start an {bcolors.BOLD}EASY{bcolors.ENDC} or {bcolors.BOLD}HARD{bcolors.ENDC} game?")
    print(f"\n{bcolors.WARNING}* Please only input {bcolors.BOLD}E{bcolors.ENDC}{bcolors.WARNING} or {bcolors.BOLD}H{bcolors.ENDC}{bcolors.WARNING}! *{bcolors.ENDC}")
    difficulty = input("\n(E / H) > ").lower()

os.system("clear")
temp_board.output()
  
while True:
  if game.turn == X:
    temp = tempX
  else:
    temp = tempO
    
  win_check = game.check_win(saved_board)
  if win_check == 0:
    if len(saved_board.free_spaces()) < 1:
      print("The game has tied.")
      break
  else:
    if win_check == 1:
      print("X has won the game!")
      break
    else:
      print("O has won the game!")
      break
  
  if game.turn == X:
    move = computer_ai.move()

    print("Thinking...")
    time.sleep(0.7)
    
    saved_board.__dict__[move] = X

    game.switch_turn()

    temp_board.reset(saved_board)
    os.system("clear")
    temp_board.a1 = tempO
    temp_board.output()
    continue
    
  print(f"It is {game.turn}'s turn.")
  
  print(f"\n{bcolors.BOLD}X{bcolors.ENDC} is {bcolors.BOLD}{bcolors.FAIL}RED{bcolors.ENDC} and {bcolors.BOLD}O{bcolors.ENDC} is {bcolors.BOLD}{bcolors.OKGREEN}GREEN{bcolors.ENDC}.")
  print(f"The selected position is {bcolors.BOLD}{bcolors.OKBLUE}BLUE{bcolors.ENDC}.")
  print(f"Use {bcolors.BOLD}ARROW KEYS{bcolors.ENDC} to select position and {bcolors.BOLD}ENTER{bcolors.ENDC} to confirm.")
  
  key = getkey()
  if key == keys.LEFT:
    if temp_board.column > 1:
      temp_board.column -= 1

    os.system('clear')
    temp_board.reset(saved_board)
    temp_board.__dict__[temp_board.row + str(temp_board.column)] = temp
    temp_board.output()
    
  if key == keys.RIGHT:
    if temp_board.column < 3:
      temp_board.column += 1

    os.system('clear')
    temp_board.reset(saved_board)
    temp_board.__dict__[temp_board.row + str(temp_board.column)] = temp
    temp_board.output()

  if key == keys.DOWN:
    if temp_board.row != "c":
      if temp_board.row == "a":
        temp_board.row = "b"
      else:
        temp_board.row = "c"

    os.system('clear')
    temp_board.reset(saved_board)
    temp_board.__dict__[temp_board.row + str(temp_board.column)] = temp
    temp_board.output()
    
  if key == keys.UP:
    if temp_board.row != "a":
      if temp_board.row == "c":
        temp_board.row = "b"
      else:
        temp_board.row = "a"

    os.system('clear')
    temp_board.reset(saved_board)
    temp_board.__dict__[temp_board.row + str(temp_board.column)] = temp
    temp_board.output()

  if key == keys.ENTER and getattr(saved_board, temp_board.row + str(temp_board.column)) == " ":
    saved_board.__dict__[temp_board.row + str(temp_board.column)] = game.turn

    temp_board.row = "a"
    temp_board.column = 1

    game.switch_turn()

    temp_board.reset(saved_board)
    os.system("clear")

    if game.turn == O:
      temp_board.a1 = tempO
    temp_board.output()
