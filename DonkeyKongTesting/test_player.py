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

class PlayerTests():		#Tests for class Board
	def test_playerspawnposn(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

		assert ( P.getY() == 1 and P.getX() == (ROWS - 2) )		#Tests if player spawn position is correct
		
	def test_playerspawndetails(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

		assert ( P.getScore() == 0 and P.getLife() == 3 and P.getLevel() == 1 ) #Tests if player score,lives and level is initialized correctly

	def test_playerrightwallcheck(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

		P.changeposn(P.getX(),COLS-2)
		array[P.getX()][P.getY()] = 4
		if array[P.getX()][P.getY()+1] == -1:
			P.changeposn(P.getX(),P.getY())
			array[P.getX()][P.getY()] = 4
		else:
			P.changeposn(P.getX(),P.getY()+1)
			array[P.getX()][P.getY()+1] = 4

		assert P.getY() != (COLS-1)

		P.changeposn(P.getX(),COLS-7)
		array[P.getX()][P.getY()] = 4
		if array[P.getX()][P.getY()+1] == -1:
			P.changeposn(P.getX(),P.getY())
			array[P.getX()][P.getY()] = 4
		else:
			P.changeposn(P.getX(),P.getY()+1)
			array[P.getX()][P.getY()+1] = 4

		assert P.getY() != (COLS-1)

	def test_playerleftwallcheck(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

		P.changeposn(P.getX(),1)
		array[P.getX()][P.getY()] = 4
		if array[P.getX()][P.getY()-1] == -1:
			P.changeposn(P.getX(),P.getY())
			array[P.getX()][P.getY()] = 4
		else:
			P.changeposn(P.getX(),P.getY()-1)
			array[P.getX()][P.getY()-1] = 4

		assert P.getY() != (0)

		P.changeposn(P.getX(),COLS-7)
		array[P.getX()][P.getY()] = 4
		if array[P.getX()][P.getY()-1] == -1:
			P.changeposn(P.getX(),P.getY())
			array[P.getX()][P.getY()] = 4
		else:
			P.changeposn(P.getX(),P.getY()-1)
			array[P.getX()][P.getY()-1] = 4

		assert P.getY() != (0)

	def test_playercollectcoin(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

			oldscore = P.getScore()

			temprow = ROWS-2
			tempcol = 1

			while True:
				if array[temprow][tempcol+1] == 3:
					break
				elif tempcol == COLS-4:
					temprow += 4
					tempcol = P.getY()
				else:
					tempcol += 1

			P.changeposn(temprow,tempcol)
			array[temprow][tempcol] = 4

			if array[P.getX()][P.getY() + 1] == 3:
				P.changeposn(temprow,tempcol)
				array[temprow][tempcol] = 4
				P.collectCoin()

			assert P.getScore() == oldscore + 5
			running = False

	def test_princessrescue(self):
		P = Player("Hello",1,ROWS - 2, COLS, 1, 0)
		newb = Board()
		array = []
		pathexists = False
		testofthree = False
		numofcoins = 0
		while True:
			pathexists,numofcoins,testofthree = newb.init(COLS,ROWS,array,P)
			if pathexists == True:
				break

			oldscore = P.getScore()

			if array[1][newb.princess] == 1:
				temprow = 1
				tempcol = newb.princess

				P.changeposn(1,newb.princess)
				array[1][newb.princess] = 4

				if P.getX() == 1 and P.getY() == newb.princess:
					P.score += 50
					if P.level == 3:
						os.system("clear")

				assert P.getScore() == oldscore + 50
				running = False

def tests():
	

	

	


	obj = PlayerTests()
	obj.test_playerspawnposn()			#Test Player spawn Position
	obj.test_playerspawndetails()		#Test Player details
	obj.test_playerrightwallcheck()	#Test Right wall collision
	obj.test_playerleftwallcheck()		#Test Left wall collision
	obj.test_playercollectcoin()		#Tests score on collect coin
	obj.test_princessrescue()			#Tests score update on pricess rescue

if __name__ == "__main__":	#Actual main function 
	tests()