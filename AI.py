# AI.py>

#Incremental: current reality
def ai(self):

  #Prevents AI getting stuck "stuck checker"
  #If same score occurs more than three times; then not tile has merged/board is not moving; AI is stuck
    if(self.recentScores.count(self.recentScores[-1]) > 3 ):

      #if the count of _turns where board does not move_ is odd
      if(self.recentScores.count(self.recentScores[-1]) % 2 == 1):
        print("Stuck, going down")
        self.lastMove = 'Down'
        return(self)
        # else if even (to alternate action)
      elif(self.recentScores.count(self.recentScores[-1]) % 2 == 0):
        print("Stuck, going right")
        self.lastMove = 'Right'
        return(self)

  #Moves pieces Up & Left
    if (self.lastMove == 'Up'):
      self.lastMove = 'Left'
    elif (self.lastMove == 'Left'):
      self.lastMove = 'Up'
    else:
      self.lastMove = 'Up'
    return (self)

  


#Experimental Ideas
def PlannedAI(self):

  #  Prototype:
  
  #Find highest value on board
  highestNum = 0
  
  for x in self.gamepanel.gridCell:
    for y in x:
      if(highestNum > y): highestNum = y

  
      

    
  for x in self.gamepanel.gridCell: print(x, "\n")
  
  return(self)