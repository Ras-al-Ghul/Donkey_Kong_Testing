#Main File
#Import section

from __future__ import print_function
from subprocess import call
from prints import colors

#import pyxhook
import random
import time
import os
import sys

from scrollingbanner import func
from prints import printboard
from classboard import Board
from playerandball import Person
from playerandball import Player
from playerandball import Donkey
from playerandball import Fireball

#Constants
#ROWS and COLUMNS can be changed to suit your taste
#**May not work for all values of rows due to random floor and stair generation**
global ROWS,COLUMNS
ROWS = 30	
COLUMNS = 80


mainarr = []
running = True



#	A:97	D:100	W:119	S:115	Q:113	Space:32
keyarr=[100,100,100,100,100]
prow=(ROWS-2)
pcol=1



stairarr = []

def kbevent(event):
	#This function is called everytime a key is pressed. The ascii value of the pressed key is compared with below values and the next course of action is decided
	#Also the coins are collected here
	#A stack (push and pop) mechanism is used to ensure that the stairs are not erased when the player uses them

	global keyarr  #To store previous key
	global stairarr	#To store stairs
	global P
	prow,pcol = P.getPosition()
	if event.Ascii == 113:
        	global running
        	running = False
		call(["stty","echo"])
		os.system("clear")
		sys.exit()
	elif event.Ascii == 97:
		keyarr.pop(0)
		keyarr.append(97)
		if P.checkWall(prow,pcol-1,mainarr) == False:
			if len(stairarr) > 0 and stairarr.pop() == 2:
				mainarr[prow][pcol] = 2
			else:			
				mainarr[prow][pcol] = 0
			if mainarr[prow][pcol-1] == 2:
				stairarr.append(2)
			pcol-=1
			P.changeposn(prow, pcol)
			if mainarr[prow][pcol] == 3:
				P.collectCoin()
			mainarr[prow][pcol]=4
			
	elif event.Ascii == 100:
		keyarr.pop(0)		
		keyarr.append(100)
		if P.checkWall(prow,pcol+1,mainarr) == False:
			if len(stairarr) > 0 and stairarr.pop() == 2:
				mainarr[prow][pcol] = 2
			else:			
				mainarr[prow][pcol] = 0
			if mainarr[prow][pcol+1] == 2:
				stairarr.append(2)		
			pcol+=1
			P.changeposn(prow, pcol)
			if mainarr[prow][pcol] == 3:
				P.collectCoin()
			mainarr[prow][pcol]=4
			
	elif event.Ascii == 119:
		keyarr.pop(0)		
		keyarr.append(119)
		if P.checkWall(prow-1,pcol,mainarr) == False and ( (mainarr[prow-1][pcol] == 2 or (mainarr[prow][pcol+1] == -1 and mainarr[prow][pcol-1] == -1)) \
							 or ((mainarr[prow][pcol-1]==(-1) or mainarr[prow][pcol+1]==(-1))and(pcol!=(COLUMNS-2) and pcol!=(1))) ):		
			if len(stairarr) > 0 and stairarr.pop() == 2:
				mainarr[prow][pcol] = 2
			else:			
				mainarr[prow][pcol] = 0
			if mainarr[prow-1][pcol] == 2:
				stairarr.append(2)		
			prow-=1
			P.changeposn(prow, pcol)
			if mainarr[prow][pcol] == 3:
				P.collectCoin()
			mainarr[prow][pcol]=4
			
	elif event.Ascii == 115:
		keyarr.pop(0)		
		keyarr.append(115)
		if P.checkWall(prow+1,pcol,mainarr) == False:
			if len(stairarr) > 0 and stairarr.pop() == 2:
				mainarr[prow][pcol] = 2
			else:			
				mainarr[prow][pcol] = 0
			if mainarr[prow+1][pcol] == 2:
				stairarr.append(2)
			prow+=1
			P.changeposn(prow, pcol)
			if mainarr[prow][pcol] == 3:
				P.collectCoin()		
			mainarr[prow][pcol]=4
			
	elif event.Ascii == 32:
		P.updown = 1
		if keyarr[4] == 100:
			if P.checkWall(prow-2,pcol+2,mainarr) == False:
				if P.checkWall(prow,pcol+4,mainarr) == False:
					
					if len(stairarr) > 0 and stairarr.pop() == 2:
						mainarr[prow][pcol] = 2
					else:			
						mainarr[prow][pcol] = 0
					
					if mainarr[prow-2][pcol+2] == 2:
						stairarr.append(2)					
					prow-=2;pcol+=2
					P.changeposn(prow, pcol)
					if mainarr[prow][pcol] == 3:
						P.collectCoin()
					mainarr[prow][pcol]=4
					time.sleep(0.1)
										
					if len(stairarr) > 0 and stairarr.pop() == 2:
						mainarr[prow][pcol] = 2
					else:			
						mainarr[prow][pcol] = 0
					if mainarr[prow+2][pcol+2] == 2: 
						stairarr.append(2)	
					prow+=2;pcol+=2
					P.changeposn(prow, pcol)
					if mainarr[prow][pcol] == 3:
						P.collectCoin()
					mainarr[prow][pcol]=4		
		elif keyarr[4] == 97:
			if P.checkWall(prow-2,pcol-2,mainarr) == False:
				if P.checkWall(prow,pcol-4,mainarr) == False:
					if len(stairarr) > 0 and stairarr.pop() == 2:
						mainarr[prow][pcol] = 2
					else:			
						mainarr[prow][pcol] = 0
					if mainarr[prow-2][pcol-2] == 2:
						stairarr.append(2)			
					prow-=2;pcol-=2
					P.changeposn(prow, pcol)
					if mainarr[prow][pcol] == 3:
						P.collectCoin()
					mainarr[prow][pcol]=4
					time.sleep(0.1)

					if len(stairarr) > 0 and stairarr.pop() == 2:
						mainarr[prow][pcol] = 2
					else:			
						mainarr[prow][pcol] = 0
					if mainarr[prow+2][pcol-2] == 2:
						stairarr.append(2)			
					prow+=2;pcol-=2
					P.changeposn(prow, pcol)
					if mainarr[prow][pcol] == 3:
						P.collectCoin()
					mainarr[prow][pcol]=4		
		else:
			if P.checkWall(prow-2,pcol,mainarr) == False:
					
				if len(stairarr) > 0 and stairarr.pop() == 2:
					mainarr[prow][pcol] = 2
				else:			
					mainarr[prow][pcol] = 0
				if mainarr[prow-2][pcol] == 2:
					stairarr.append(2)						
				prow-=2
				P.changeposn(prow, pcol)
				if mainarr[prow][pcol] == 3:
					P.collectCoin()
				mainarr[prow][pcol]=4
				time.sleep(0.08)

				if len(stairarr) > 0 and stairarr.pop() == 2:
					mainarr[prow][pcol] = 2
				else:			
					mainarr[prow][pcol] = 0
				if mainarr[prow+2][pcol] == 2:
					stairarr.append(2)		
				prow+=2
				P.changeposn(prow, pcol)
				if mainarr[prow][pcol] == 3:
					P.collectCoin()
				mainarr[prow][pcol]=4
		P.updown = 0		

def levelVar(P):	#Set level dependant variables
	if P.level == 1:
		return 1,4,1
	elif P.level == 2:
		return 2,6,2
	else:
		return 3,6,3

def createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newboard,mainarr,COLUMNS,dobjectarr,upint):	#Creates 1,2,3 donkeys depending on level
	while counter < numofdonkeys:
		dindexarr[counter],dlenarr[counter] = newboard.forDonkey(counter)
		dobjectarr[counter]=Donkey("hello",dindexarr[counter],(dindexarr[counter]+dlenarr[counter])%COLUMNS,5+(counter*4),COLUMNS, mainarr)
		counter += 1
	return dindexarr,dlenarr,counter

def createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLUMNS, fbarr, upint,mainarr):		#Creates variable number of fireballs depending on level
		ball2time = time.time()
		if currball < numofball and random.randint(1,10) > 8:
			temprand = random.randint(1,upint)
			temprand -= 1			
			if dobjectarr[temprand] == 0:
				return dobjectarr,ball1time,currball,fbarr
			if ball2time - ball1time > 3 and dobjectarr[temprand].getX() != 0 and dobjectarr[temprand].getY() != 1 and \
					dobjectarr[temprand].getY() != (COLUMNS-1) and dobjectarr[temprand].getY() != (COLUMNS-2):					
				fbarr[currball] = Fireball(dobjectarr[temprand].getX(),dobjectarr[temprand].getY(),mainarr,dobjectarr[temprand].direction)
				currball += 1
				ball1time = time.time()
		return dobjectarr,ball1time,currball,fbarr

def updateBalls(mainarr,fbarr,ROWS,COLUMNS,dobjectarr):		#Updates the position of the fireballs 
		for i in fbarr:
			if i != 0:
				if i.getX() == (ROWS - 2) and i.getY() == 1:
					mainarr[i.getX()][i.getY()] = 0
					if dobjectarr[0] != 0:					
						i.changeposn(dobjectarr[0].getX(),dobjectarr[0].getY())
						if dobjectarr[0].direction == 1:
							i.direction = 2
						else:
							i.direction = 1
					continue
				if mainarr[i.getX()+1][i.getY()] != -1 and mainarr[i.getX()+1][i.getY()] != 2:			
						mainarr[i.getX()][i.getY()] = 0									
						mainarr[i.getX()+1][i.getY()] = 6
						i.changeposn(i.getX()+1,i.getY())				
				elif mainarr[i.getX()+1][i.getY()] == 2 and len(i.larray) == 0:
					if mainarr[i.getX()+3][i.getY()] != 2:
						i.autoPath(mainarr)
					else:
						if random.randint(0,1) == 1:
							if len(i.miscarr) > 0:
								mainarr[i.getX()][i.getY()] = (i.miscarr).pop()
							else:
								mainarr[i.getX()][i.getY()] = 0				
							(i.larray).append(mainarr[i.getX()+1][i.getY()])
							mainarr[i.getX()+1][i.getY()] = 6
							i.changeposn(i.getX()+1,i.getY())
							continue
						else:
							i.autoPath(mainarr)
				elif mainarr[i.getX()+1][i.getY()] == 2 and len(i.larray) != 0:
					mainarr[i.getX()][i.getY()] = (i.larray).pop()
					(i.larray).append(mainarr[i.getX()+1][i.getY()])
					mainarr[i.getX()+1][i.getY()] = 6
					i.changeposn(i.getX()+1,i.getY())
					continue
				elif mainarr[i.getX()+1][i.getY()] == -1 and len(i.larray) != 0:
					if mainarr[i.getX()][i.getY()+1] == 0:
						mainarr[i.getX()][i.getY()] = (i.larray).pop()
						mainarr[i.getX()][i.getY()+1] = 6
						i.changeposn(i.getX(),i.getY()+1)
					else:
						mainarr[i.getX()][i.getY()] = (i.larray).pop()
						mainarr[i.getX()][i.getY()-1] = 6
						i.changeposn(i.getX(),i.getY()-1)
				i.autoPath(mainarr)
		return mainarr,fbarr

def mainfunc(level,pname,score):	#Tertiary main function. Contains the main while loop
	
	#Create hookmanager
	hookman = pyxhook.HookManager()
	#Define our callback to fire when a key is pressed down
	hookman.KeyDown = kbevent
	#Hook the keyboard
	hookman.HookKeyboard()
	#Start our listener
	hookman.start()	

	global ball1time,ball2time
	ball1time = time.time()		#These ensure that the balls are produced after a time gap and not all together
	
	global P	
	P = Player(pname, ROWS-2, 1,COLUMNS, level,score)	#Instantiating Player
	
	#Create new layout
	global newboard,mainarr
	while True:
		mainarr = []
		newboard = Board()
		pathexists, numofcoins, testofthree = newboard.init(COLUMNS,ROWS,mainarr,P)
		if pathexists == True:	#Creating board and ensuring that there exists a path from player spawn position to the princess
			break
	
	global numofdonkeys,numofball,upint
	numofdonkeys,numofball,upint = levelVar(P)
	
	dindexarr = [0,0,0]
	dlenarr = [0,0,0]
	global dobjectarr
	dobjectarr = [0,0,0]	
	
	global fbarr
	fbarr = [0,0,0,0,0,0,0,0]
	global currball 
	currball = 0	

	global counter
	counter = 0
	
	dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newboard,mainarr,COLUMNS,dobjectarr,upint)	#Create donkeys

	oldtime=time.time()	#To judge jump direction
	
	global keyarr
	global running

	running = True
	while running:		#Main while loop
		os.system("clear")
	
		newtime=time.time()	#To judge jump direction when the spacebar is pressed
		if (newtime-oldtime) > 1:
			keyarr.pop(0)
			keyarr.append(115)
			oldtime=newtime
		
		#Choose what to do depending on current variable values		

		if P.life == 0:
			os.system("clear")			
			hookman.cancel()
			return (-1),P.score
	
		if P.getX() == 1 and P.getY() == newboard.princess:
			P.score += 50
			if P.level == 3:
				os.system("clear")
				func(3, P.score)
				hookman.cancel()				
				return (-1),P.score
			hookman.cancel()
			return P.level+1,P.score

		if mainarr[P.getX()][P.getY()+1] == 6 or mainarr[P.getX()][P.getY()-1] == 6:
			mainarr[P.getX()][P.getY()] = 0
			P.life -= 1
			P.changeposn(ROWS - 2, 1)
			mainarr[P.getX()][P.getY()] = 4
			P.score -= 25
			continue

		tempr,tempcol = P.getPosition()
		if mainarr[tempr+1][tempcol] != -1 and mainarr[tempr+1][tempcol] != 2 and P.updown != 1:
			mainarr[tempr][tempcol] = 0
			mainarr[tempr+1][tempcol] = 4
			P.changeposn(tempr+1,tempcol)
		
		global note
		note = -1
		tempindex = 0
		for i in dobjectarr:
			if i != 0:			
				if i.checkCollision(mainarr) == True:
					i.killDonkey(mainarr,P)					
					note = 1
					break
				else:
					i.donkeyWalk(mainarr)
			tempindex += 1		
		
		if note != -1:
			dobjectarr[tempindex] = 0
			P.score += 25
			note = -1
	
		#ball section
		
		
		ball2time = time.time()
		dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLUMNS, fbarr, upint, mainarr)
			
		mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLUMNS,dobjectarr)
		
		printboard(COLUMNS, ROWS, mainarr, P)	#Print the board

		time.sleep(0.12)

	
		
	#Close the listener when we are done
	hookman.cancel()
	sys.exit()

def main():	#Secondary main function to help in calling and returning
	global returnval
	returnval = func(1,-1)
	if returnval == 1:
		os.system("clear")
		
		global name
		oldname = raw_input(colors.YELLOW+colors.BOLD+"Enter Player name : "+colors.BLUE)	
		name = oldname.replace("n", "")	
		
		call(["stty","-echo"])	#To prevent lag	

		global savemem,scores		
		savemem = 1
		scores = 0

		while savemem != -1:
			savemem,scores = mainfunc(savemem,name,scores)

		if savemem == -1:
			tempcheck = 0
			while returnval == 1:
				if tempcheck == 0:				
					returnval = func(2,scores)
					savemem = 1
					scores = 0
				savemem,scores = mainfunc(savemem,name,scores)
				if savemem != -1:
					tempcheck = 1
				else:
					tempcheck = 0
					
			if returnval == 2:
				call(["stty","echo"])
				sys.exit()
		else:
			call(["stty","echo"])
			sys.exit()

	else:
		sys.exit()
	
	call(["stty","echo"])
	sys.exit()

if __name__ == "__main__":	#Actual main function 
	main()
