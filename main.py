#################################################################
# Welcome to Scott's version of the Rock, Paper, Scissors Game! #
#################################################################


import random # library needed to generate computer's turn
import os
import time


def displayChoice(choice):
# Simple function to display move choice for either player or CPU
  if choice == 0:
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
         Rock
    '''
    print(rock)
  elif choice == 1:
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    
          Paper
    '''
    print(paper)
  else:
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    
        Scissors
    '''
    print(scissors)

def getCPU_move():
# Simple function to generate CPU move and return its value
  cpuTurn = random.randint(0, 2)
  return(cpuTurn)
  
def getUser_move():
# Prompt user for move and return value.  Only accept valid input.
    
    userTurn = -1 # initialize userTurn to force entry into the loop
    validChoices = [0, 1, 2] # user can only select these 3 options
    while userTurn not in validChoices: # loop to validate user input
        try:
            userTurn = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'))
            if userTurn < 0 or userTurn > 2:
                print('\nError: Please enter a number between 0-2.\n')
        except ValueError:
            print('\nError: Please enter a number between 0-2.\n')
    return(userTurn)

def getWinner(player, computer):
# receives player and CPU moves and determines winner
# if player wins return True, if CPU wins return False
    
  if player > computer: # higher choice generally wins
      # except when CPU chose rock, player chose scissors
    if computer == 0 and player == 2:
      return(False) # CPU wins
    else:
      return(True)
  else:
    if player == 0 and computer == 2: # player chose rock, CPU chose scissors
      return(True) # player wins
    else:
      return(False)
    
#########################################
# Starts the game, placed inside loop   #
# to allow user to play multiple times. #
#########################################

playAgain = True
while playAgain == True:
  os.system('clear')
  print('Welcome to Scott\'s Rock, Paper, Scissors Game!\n\n')
  playerName = input('Who\'s playing today?\n')
  print(f'\nGood luck {playerName}, you\'re going to need it!')

# Gets player and CPU moves   
  print(f'\nIt\'s your turn {playerName}!\n')
  playerMove = getUser_move()
  cpuMove = getCPU_move()
  
  os.system('clear')
  print('Rock, Paper, Scissors SHOOT!\n')
  time.sleep(1)

# Displays player and CPU choices
  print(f'{playerName} chose:\n')
  displayChoice(playerMove)
    
  print('\nMy choice was:\n')
  displayChoice(cpuMove)
  
  print('And the results are...\n\n')
  time.sleep(.5)

# Determine who the winner is
  if playerMove != cpuMove:
    winner = getWinner(playerMove, cpuMove)
    if winner == True:
      print(f'Congrats {playerName}, you are the winner!\n')
    else:
      print(f'Sorry {playerName}, I am the winner!\n')
  else:
    print(f'Hey {playerName}, it\'s a TIE game!\n')
  
# Prompt the user if they want to play again.
# Placed in a loop to validate user input and
# only accept 'y' or 'n' values
  gameChoice = ''
  while gameChoice.lower() != 'y' or gameChoice.lower() != 'n':
    gameChoice = input('\nWould you like to play again? Y/N\n')
    if gameChoice.lower() == 'y':
        playAgain = True
        break
    elif gameChoice.lower() == 'n':
        print(f'\nThanks for playing {playerName}, that was fun!')
        playAgain = False
        break
    else:
        print('Error:  Please enter a \'y\' or \'n\'\n')
  

