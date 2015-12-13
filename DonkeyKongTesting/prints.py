#This file houses the print function

from __future__ import print_function
from playerandball import Player

class colors:
    	RED = '\033[91m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	WHITE = '\033[97m'
	YELLOW = '\033[93m'
	GREY = '\033[90m'
	BLACK = '\033[90m'
	DEFAULT = '\033[99m'
	PURPLE = '\033[95m'
    	ENDC = '\033[0m'
    	BOLD = '\033[1m'
    	UNDERLINE = '\033[4m'

def printboard(cols, rows, array, P):
	print(colors.BOLD+colors.YELLOW+"				DONKEY KONG")	
	for i in range(rows):
        	for j in range(cols):
        	    if array[i][j] == -1:
        	        print(colors.BLACK+colors.BOLD+"X"+colors.ENDC, end="")	#Print wall
        	    elif array[i][j] == 1:
        	        print(colors.WHITE+colors.BOLD+"Q"+colors.ENDC, end="")	#Print Princess
		    elif array[i][j] == 2:
			print(colors.GREEN+colors.BOLD+"H"+colors.ENDC, end="")	#Print Stair
		    elif array[i][j] == 3:
			print(colors.YELLOW+colors.BOLD+"C"+colors.ENDC, end="")	#Print Coin
		    elif array[i][j] == 4:
			print(colors.CYAN+colors.BOLD+"P"+colors.ENDC, end=""+colors.ENDC)	#Print Player
		    elif array[i][j] == 5:
			print(colors.BLUE+colors.BOLD+"D"+colors.ENDC, end="")	#Print Donkey
		    elif array[i][j] == 6:	
			print(colors.RED+colors.BOLD+"O"+colors.ENDC, end="")	#Print Fireball
        	    else:
        	        print(" ", end="")	#Print blank space
        	print("\n",end="")

	print(colors.BOLD+colors.YELLOW+str(P.getName())+colors.BOLD+colors.BLUE+"			   SCORE "+colors.BOLD+colors.YELLOW + str(P.getScore())+colors.BOLD+colors.BLUE+"	  LEVEL "+colors.BOLD+colors.YELLOW + str(P.getLevel())+colors.BOLD+colors.BLUE+"			 LIVES "+colors.BOLD+colors.YELLOW + str(P.getLife())+colors.ENDC)	
    	
    
	
