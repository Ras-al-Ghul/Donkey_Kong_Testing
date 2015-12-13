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

class DonkeyTests():
	def test_donkeyandwall(self):
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
					
			for i in dobjectarr:
				if i != 0:			
					oldtempx,oldtempy = i.getPosition()
					i.donkeyWalk(mainarr)
					tempx,tempy = i.getPosition()
					assert tempx == oldtempx
					if (time.time() - starttime) > 10:
						running = False

	def test_donkeyandplayer(self):
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
					
			note = -1
			tempindex = 0
			for i in dobjectarr:
				if i != 0:	
					if i.getdir() == 1:
						P.changeposn(i.getX(),i.getY()+1)
						mainarr[i.getX()][i.getY()+1] = 4
					else:
						P.changeposn(i.getX(),i.getY()-1)
						mainarr[i.getX()][i.getY()-1] = 4
					assert i.checkCollision(mainarr) == True
					if i.checkCollision(mainarr) == True:
						i.killDonkey(mainarr,P)					
						note = 1
						running = False
						break
					else:
						i.donkeyWalk(mainarr)
				tempindex += 1		
			
			if note != -1:
				dobjectarr[tempindex] = 0
				P.score += 25
				note = -1

	def test_donkeyinitposn(self):
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
					
			note = -1
			tempindex = 0
			for i in dobjectarr:
				if i != 0:	
					assert i.getX() == 4
					running = False

	def test_donkeyplayerlife(self):
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
					
			oldlife = P.getLife()

			note = -1
			tempindex = 0
			for i in dobjectarr:
				if i != 0:	
					if i.getdir() == 1:
						P.changeposn(i.getX(),i.getY()+1)
						mainarr[i.getX()][i.getY()+1] = 4
					else:
						P.changeposn(i.getX(),i.getY()-1)
						mainarr[i.getX()][i.getY()-1] = 4
					
					if i.checkCollision(mainarr) == True:
						i.killDonkey(mainarr,P)					
						note = 1
						running = False
						break
					else:
						i.donkeyWalk(mainarr)
				tempindex += 1		
			
			assert P.getLife() == oldlife

			if note != -1:
				dobjectarr[tempindex] = 0
				P.score += 25
				note = -1

	def test_numofdonkeys(self):
		
		P = Player("Hello",1,ROWS - 2, COLS, 2, 0)
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

		running = True
		while running:		#Main while loop

			tempcnt = 0
			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)
					tempcnt += 1

			assert tempcnt == numofdonkeys
			running = False

		P = Player("Hello",1,ROWS - 2, COLS, 3, 0)
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

		running = True
		while running:		#Main while loop

			tempcnt = 0
			for i in dobjectarr:
				if i != 0:			
					i.donkeyWalk(mainarr)
					tempcnt += 1

			assert tempcnt == numofdonkeys
			running = False


def tests():
	obj = DonkeyTests()
	obj.test_donkeyandwall()		#Test Donkey's movement, should not fall of floor
	obj.test_donkeyandplayer()		#Test Donkey collision with Player, Donkey should die
	obj.test_donkeyinitposn()		#Test Donkey spawn position
	obj.test_donkeyplayerlife()	#Test if Player loses life on collision with Donkey, which shouldn't happen
	obj.test_numofdonkeys()		#Tests if the number of donkeys increases per level


if __name__ == "__main__":	#Actual main function 
	tests()