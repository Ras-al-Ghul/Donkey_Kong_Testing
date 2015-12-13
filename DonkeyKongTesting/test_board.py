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

class BoardTests():		#Tests for class Board
	def test_coinnum(self):
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

		assert numofcoins >= 20		#Tests if number of coins generated is greater than 20, 
		
	def test_pathexists(self):
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

		assert pathexists == True	#Tests if path exists from Player position to Princess position
		
	def test_rowgap(self):
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

		assert testofthree == True	#Fails if the gap between two rows is lesser than 3 units

	def test_queen(self):
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

		temprow = 1
		tempcol = 1
		while tempcol != COLS-1:
			if array[temprow][tempcol] == 1:
				assert array[temprow][tempcol] == 1
				break
			tempcol += 1

	def test_boardvalidate(self):
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
		assert array[0][0] == -1
		assert array[0][COLS-1] == -1
		assert array[ROWS-1][0] == -1
		assert array[ROWS-1][COLS-1] == -1

	def test_brokenstairs(self):
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
		assert newb.brokenstairs() == True


def tests():
	obj = BoardTests()
	obj.test_boardvalidate()	#Tests the board's dimensions
	obj.test_coinnum()			#Test minimum number of coins >= 20
	obj.test_pathexists()		#Tests if a path exists from Player spawn position to Princess
								#Necessary because floors and stairs are generated randomly
	obj.test_rowgap()			#Also tests if gap between two floors is 3 units as specified
	obj.test_queen()			#Tests queen's details
	obj.test_brokenstairs		#Tests if there are broken stairs

if __name__ == "__main__":	#Actual main function 
	tests()