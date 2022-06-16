from TwentyFortyEight import *
from tetris import *

Gamestart = True


while Gamestart == True:
    try:
        OneGame = game.score
        TwoGame = gamepanel.score
        TetrisScore = OneGame
        twentyfortyeightscore = TwoGame
    except NameError:
        print("You Broke the Game : (")
        Gamestart = False


