from tkinter import *
from tkinter import messagebox
import random

#For AI assignment:
from AI import *

from BoardClass import *

#Game
class Game:

  def __init__(self, gamepanel):
    self.gamepanel = gamepanel
    self.end = False
    self.won = False

      #Added for AI:
    #Holds the last move made/input to the game board
    self.lastMove = 'Up'
    #Holds all scores made during the game
    self.recentScores = [0]
              #(Optional info):  #The 0 is to allow the AI to use the "stuck checker" on the first turn

  def start(self):
    self.gamepanel.random_cell()
    self.gamepanel.random_cell()
    self.gamepanel.paintGrid()
    self.gamepanel.window.bind('<Key>', self.link_keys)
    self.gamepanel.window.mainloop()

    
  # Runs the game; updates the board for each move made by the user; the central nervous system.
  def link_keys(self, event):
    if self.end or self.won:
      return

    self.gamepanel.compress = False
    self.gamepanel.merge = False
    self.gamepanel.moved = False


    
 ###################################################
###AI PLUGS IN HERE     
#Use one input not both!
    
    #AI INPUT, with human override

    temp = event.keysym

    if(temp == 'space'):
      self = ai(self)
      presed_key = self.lastMove
    else:
      print("Human input")
      presed_key = temp
      
    #HUMAN INPUT
    #presed_key = event.keysym
    

    

    if presed_key == 'Up':
      self.gamepanel.transpose()
      self.gamepanel.compressGrid()
      self.gamepanel.mergeGrid()
      self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
      self.gamepanel.compressGrid()
      self.gamepanel.transpose()

    elif presed_key == 'Down':
      self.gamepanel.transpose()
      self.gamepanel.reverse()
      self.gamepanel.compressGrid()
      self.gamepanel.mergeGrid()
      self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
      self.gamepanel.compressGrid()
      self.gamepanel.reverse()
      self.gamepanel.transpose()

    elif presed_key == 'Left':
      self.gamepanel.compressGrid()
      self.gamepanel.mergeGrid()
      self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
      self.gamepanel.compressGrid()

    elif presed_key == 'Right':
      self.gamepanel.reverse()
      self.gamepanel.compressGrid()
      self.gamepanel.mergeGrid()
      self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
      self.gamepanel.compressGrid()
      self.gamepanel.reverse()
    else:
      pass

    self.gamepanel.paintGrid()
    print(self.gamepanel.score)
    #Added for AI
    self.recentScores.append(self.gamepanel.score)


    #Determines if the game was won!
    # ...it seems inefficient, but I don't think I should touch it.
    flag = 0
    for i in range(4):
      for j in range(4):
        if (self.gamepanel.gridCell[i][j] == 2048):
          flag = 1
          break

    if (flag == 1):  #found 2048
      self.won = True
      messagebox.showinfo('2048', message='You Wonnn!!')
      print("won")
      return


    #Game lost
    for i in range(4):
      for j in range(4):
        if self.gamepanel.gridCell[i][j] == 0:
          flag = 1
          break

    if not (flag or self.gamepanel.can_merge()):
      self.end = True
      messagebox.showinfo('2048', 'Game Over!!!')
      print("Over")

      
    #Adds 2 to random position
    if self.gamepanel.moved:
      self.gamepanel.random_cell()

    
    self.gamepanel.paintGrid()


gamepanel = Board()
game2048 = Game(gamepanel)
game2048.start()
