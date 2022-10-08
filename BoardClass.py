##DO NOT MODIFY
##DO NOT MODIFY
##DO NOT MODIFY
##DO NOT MODIFY

#From original game
#Put in seperate file to allow AI to import functions

from tkinter import *
from tkinter import messagebox
import random


class Board:
  bg_color = {
    '2': '#eee4da',
    '4': '#ede0c8',
    '8': '#edc850',
    '16': '#edc53f',
    '32': '#f67c5f',
    '64': '#f65e3b',
    '128': '#edcf72',
    '256': '#edcc61',
    '512': '#f2b179',
    '1024': '#f59563',
    '2048': '#edc22e',
  }
  color = {
    '2': '#776e65',
    '4': '#f9f6f2',
    '8': '#f9f6f2',
    '16': '#f9f6f2',
    '32': '#f9f6f2',
    '64': '#f9f6f2',
    '128': '#f9f6f2',
    '256': '#f9f6f2',
    '512': '#776e65',
    '1024': '#f9f6f2',
    '2048': '#f9f6f2',
  }

  def __init__(self):
    #holds data for the board
    #Original; from game
    # Python objects
    self.window = Tk()
    self.window.title('ProjectGurukul 2048 Game')
    self.gameArea = Frame(self.window, bg='azure3')
    # Custom objects
    self.board = []
    self.gridCell = [[0] * 4 for i in range(4)]
    self.compress = False
    self.merge = False
    self.moved = False
    self.score = 0

    for i in range(4):
      rows = []
      for j in range(4):
        l = Label(self.gameArea,
                  text='',
                  bg='azure4',
                  font=('arial', 22, 'bold'),
                  width=4,
                  height=2)
        l.grid(row=i, column=j, padx=7, pady=7)

        rows.append(l)
      self.board.append(rows)
    self.gameArea.grid()

  def reverse(self):
    for ind in range(4):
      i = 0
      j = 3
      while (i < j):
        self.gridCell[ind][i], self.gridCell[ind][j] = self.gridCell[ind][
          j], self.gridCell[ind][i]
        i += 1
        j -= 1

  def transpose(self):
    self.gridCell = [list(t) for t in zip(*self.gridCell)]

  def compressGrid(self):
    self.compress = False
    temp = [[0] * 4 for i in range(4)]
    for i in range(4):
      cnt = 0
      for j in range(4):
        if self.gridCell[i][j] != 0:
          temp[i][cnt] = self.gridCell[i][j]
          if cnt != j:
            self.compress = True
          cnt += 1
    self.gridCell = temp

  # Changes the grid for the board; I think it updates the numbers; not sure if it changes their positons
  def mergeGrid(self):
    self.merge = False
    for i in range(4):
      for j in range(4 - 1):
        if self.gridCell[i][j] == self.gridCell[i][
            j + 1] and self.gridCell[i][j] != 0:
          self.gridCell[i][j] *= 2
          self.gridCell[i][j + 1] = 0
          self.score += self.gridCell[i][j]
          self.merge = True

  #Places 2s
  def random_cell(self):
    cells = []
    for i in range(4):
      for j in range(4):
        if self.gridCell[i][j] == 0:
          cells.append((i, j))
    curr = random.choice(cells)
    i = curr[0]
    j = curr[1]
    self.gridCell[i][j] = 2

  #Determines if two tiles can merge
  def can_merge(self):
    for i in range(4):
      for j in range(3):
        if self.gridCell[i][j] == self.gridCell[i][j + 1]:
          return True

    for i in range(3):
      for j in range(4):
        if self.gridCell[i + 1][j] == self.gridCell[i][j]:
          return True
    return False

  #Colors board for user
  def paintGrid(self):
    for i in range(4):
      for j in range(4):
        if self.gridCell[i][j] == 0:
          self.board[i][j].config(text='', bg='azure4')
        else:
          self.board[i][j].config(text=str(self.gridCell[i][j]),
                                  bg=self.bg_color.get(str(
                                    self.gridCell[i][j])),
                                  fg=self.color.get(str(self.gridCell[i][j])))
