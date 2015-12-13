#This file contains print calls to print the opening and ending screens

import os
#import pyxhook
import time
import sys
from subprocess import call
from prints import colors


def kbevent(event):
    		global key	#variable which controls the loop
		if event.Ascii == 110:        	
			key = 1
		elif event.Ascii == 113:
			os.system("clear")
			key = 2
		else:
			key = 0

def func(var,scores):
		global key
		key = 0	
	
		global hookman
		hookman = pyxhook.HookManager()
		hookman.KeyDown = kbevent
		hookman.HookKeyboard()
		hookman.start()		
		
		ranges = 7 #7 line banner
	
		#the width of the display
		WIDTH = 79
	
		#the message we wish to print
		if var == 1:
			message = "donkey kong".upper()
		elif var == 2:
			message = "game over".upper()
		elif var == 3:
			message = "well done!!".upper()
		else:
			message = "donkey kong".upper()
		
		
		#this is a 7-line display, stored as 7 strings
		printedMessage = [ "","","","","","","","","","","" ]
		
		#a dictionary mapping letters to their 7-linebanner display equivalents.
		characters = { " " : [ " ",
		                       " ",
		                       " ",
		                       " ",
		                       " ",
		                       " ",
		                       " " ],
	
			       "W" : [ "*     *",
		                       "*     *",
		                       "*     *",
		                       "*  *  *",
		                       "*  *  *",
	        	               "*  *  *",
	        	               "*******" ],
	
			       "L" : [ "*     ",
		                       "*     ",
		                       "*     ",
		                       "*     ",
		                       "*     ",
	        	               "*     ",
	        	               "******" ],
	
		
		               "E" : [ "*****",
		                       "*    ",
		                       "*    ",
		                       "*****",
		                       "*    ",
	        	               "*    ",
	        	               "*****" ],
	        	       
	        	       "H" : [ "*   *",
	        	               "*   *",
	        	               "*   *",
	        	               "*****",
	        	               "*   *",
	        	               "*   *",
	        	               "*   *" ], 
		
	        	       "O" : [ "*****",
	        	               "*   *",
	        	               "*   *",
	        	               "*   *",
	        	               "*   *",
	        	               "*   *",
	        	               "*****" ],
		
	        	       "L" : [ "*    ",
	        	               "*    ",
	        	               "*    ",
	        	               "*    ",
	        	               "*    ",
	        	               "*    ",
	        	               "*****" ],
	
	        	       "!" : [ "  *  ",
	        	               "  *  ",
	        	               "  *  ",
	        	               "  *  ",
	        	               "  *  ",
	        	               "     ",
	        	               "  *  " ],
			
				"D" : [ "***** ",
	        	                "*    *",
	        	                "*    *",
	        	                "*    *",
	        	                "*    *",
	        	                "*    *",
	        	                "***** " ],
				
			       "N" : [ "*     *",
	        	               "**    *",
	        	               "* *   *",
	        	               "*  *  *",
	        	               "*   * *",
	        	               "*    **",
	        	               "*     *" ], 
				"K" : ["*  *",
	        	               "* * ",
	        	               "**  ",
	       		               "*   ",
	       		               "**  ",
	       		               "* * ",
	    		               "*  *" ], 
				"G" : ["**** ",
		                       "*    ",
		                       "*    ",
		                       "*    ",
		                       "* ***",
		                       "*   *",
		                       "*****" ], 
				"Y" : ["*   *",
		                       "*   *",
	                   	       "*   *",
		                       "*****",
	        	               "    *",
	        	               "    *",
	        	               "*****" ],
				"A" : ["*****",
		                       "*   *",
	                   	       "*   *",
		                       "*****",
	        	               "*   *",
	        	               "*   *",
	        	               "*   *" ],
				"M" : ["********",
		                       "*  *   *",
	                   	       "*  *   *",
		                       "*  *   *",
	        	               "*      *",
	        	               "*      *",
	        	               "*      *" ],
				"V" : ["*   *",
		                       "*   *",
	                   	       "*   *",
		                       "*   *",
	        	               "*   *",
	        	               " * * ",
	        	               "  *  " ],
				"R" : ["*****",
		                       "*   *",
	                   	       "*   *",
		                       "*****",
	        	               "* *  ",
	        	               "*  * ",
	        	               "*   *" ]
	        	       
	        	       }
	
		#build up the printed banner. 
		for row in range(ranges):
		    for char in message:
		        printedMessage[row] += (str(characters[char][row]) + "  ")
		
		#the offset is how far to the right we want to print the message.
		offset = WIDTH
		while True:
		    #loop controls
		    if key == 1:
			hookman.cancel()
			return 1
		    elif key == 2:
			os.system("clear")
			hookman.cancel()
			call(["stty","echo"])
			sys.exit()
			return 2
	
		    os.system("clear")
		    #print each line of the message, including the offset.
		    if scores != -1:
			print(colors.BLUE+colors.BOLD+"Your score is " +colors.YELLOW+colors.BOLD+ str(scores))
			
		    for row in range(ranges):
		        print(" " * offset +colors.YELLOW+colors.BOLD+printedMessage[row][max(0,offset*-1):WIDTH - offset]+colors.ENDC)
		
		    print(colors.BLUE+colors.BOLD+"\nPress \"n\" for starting new game and \"q\" for quitting. See readme for more details.. "+colors.ENDC)
		    #move the message a little to the left.
		    offset -=1
	
		    #if the entire message has moved 'through' the display then start again from the right hand side.
		    if offset <= ((len(message)+2)*6) * -1:
		        offset = WIDTH
		    #speed up / slow down the display
		    time.sleep(0.05)
			
		hookman.cancel()
