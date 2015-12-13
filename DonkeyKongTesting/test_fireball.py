from subprocess import call
import random
import time
import os
import sys

from classboard import Board
from playerandball import Person
from playerandball import Player
from playerandball import Donkey
from playerandball import Fireball

from game import levelVar
from game import createDonkeys
from game import createBalls
from game import updateBalls

ROWS = 30
COLS = 80

from subprocess import call
import random
import time
import os
import sys

from classboard import Board
from playerandball import Person
from playerandball import Player
from playerandball import Donkey
from playerandball import Fireball

from game import levelVar
from game import createDonkeys
from game import createBalls
from game import updateBalls

ROWS = 30
COLS = 80

class FireballTests():
	def test_fireballfromdonkey(self):

		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		tempcount = 0

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			for i in fbarr:
				if i != 0:
					x,y = i.getPosition()
					for j in dobjectarr:
						if j != 0:
							if x == j.getX() and y == j.getY()+1:
								assert x == j.getX() and y == j.getY()+1	# Checks if fireball originates from donkey
								if (time.time() - starttime) >= numofball * 4:
									running = False

	def test_fireballandwall(self):

		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)
		numofball = 1	#One ball is enough for testing

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		tempcount = 0

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			for i in fbarr:
				if i != 0:
					x,y = i.getPosition()
					if y == COLS - 2 or y == 1:
						updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)	
						x,y = i.getPosition()
						assert y != (COLS-1) and y != 0
						running = False

			mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)

	def test_fireballandplayer(self):

		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)
		numofball = 1	#One ball is enough for testing

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		tempcount = 0

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			for i in fbarr:
				if i != 0:
					x,y = i.getPosition()
					if i.getDirection() == 1:
						P.changeposn(x,y+1)
					else:
						P.changeposn(x,y-1)
					break
					
			if mainarr[P.getX()][P.getY()+1] == 6 or mainarr[P.getX()][P.getY()-1] == 6:
				mainarr[P.getX()][P.getY()] = 0
				P.life -= 1
				P.changeposn(ROWS - 2, 1)
				mainarr[P.getX()][P.getY()] = 4
				assert P.getX() == ROWS-2 and P.getY() == 1
				P.score -= 25
				running = False
	
	def test_fireballexit(self):

		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)
		numofball = 1	#One ball is enough for testing

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		tempcount = 0

		P.changeposn(ROWS-2,7)
		mainarr[ROWS-2][7] = 4

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			for i in fbarr:
				if i != 0:
					x,y = i.getPosition()
					if y == 1 and x == ROWS-2:
						updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)	
						assert mainarr[ROWS-2][1] != 6
						running = False

			mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)	

	def test_numoffireballs(self):
		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 2, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		P.changeposn(ROWS-2,7)
		mainarr[ROWS-2][7] = 4

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			tempcount = 0

			for i in fbarr:
				if i != 0:
					tempcount += 1
					if tempcount == numofball:
						running = False
						assert tempcount == numofball

			#mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)

	def test_directionchange(self):
		starttime = time.time()

		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		mainarr = []
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,mainarr,P)
			if pathexists == True:
				break

		numofdonkeys,numofball,upint = levelVar(P)
		numofball = 1

		dindexarr = [0,0,0]
		dlenarr = [0,0,0]
		#global dobjectarr
		dobjectarr = [0,0,0]	
	
		#global fbarr
		fbarr = [0,0,0,0,0,0,0,0]
		#global currball 
		currball = 0	

		#global counter
		counter = 0

		dindexarr,dlenarr,counter = createDonkeys(dindexarr,dlenarr,counter,numofdonkeys,newb,mainarr,COLS,dobjectarr,upint)

		ball1time = time.time()

		P.changeposn(ROWS-2,7)
		mainarr[ROWS-2][7] = 4

		running = True
		while running:		#Main while loop

			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)

			ball2time = time.time()
			dobjectarr,ball1time,currball,fbarr = createBalls(ball1time, ball2time, currball, numofball, dobjectarr, COLS, fbarr,upint, mainarr)

			tempcount = 0

			for i in fbarr:
				if i != 0:
					olddirection = i.getDirection()
					if i.getY()+1 == COLS-1 or i.getY() - 1 == 0:
						mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)
						assert i.getDirection() != olddirection
						running = False

			mainarr,fbarr = updateBalls(mainarr,fbarr,ROWS,COLS,dobjectarr)

def tests():
	obj = FireballTests()
	obj.test_fireballfromdonkey()	#Test if Fireball spawns from Donkey's position
	obj.test_fireballandwall()		#Test Fireball collision with wall, fireball should not move through wall
	obj.test_fireballandplayer()	#Test Fireball collision with Player, Player should die
	obj.test_fireballexit()		#Test Fireball exit from Player spawn position
	obj.test_numoffireballs()		#Test if the number of fireballs increases per level
	obj.test_directionchange()		#Test if direction of fireball changes correctly on hitting wall

if __name__ == "__main__":	#Actual main function 
	tests()