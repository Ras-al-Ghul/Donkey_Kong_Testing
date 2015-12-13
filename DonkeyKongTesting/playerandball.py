#This file contains the Person, Player, Donkey and Fireball classes
#Implements OOP concepts

import random

class Person:
	def __init__(self, name, posnx, posny):    # Constructor of the class
        	self.__name = name	#The name of the object
		self.__posnx = posnx	#The xcoordinate
		self.__posny = posny	#The ycoordinate
	
	def getX(self):
		return self.__posnx
	
	def getY(self):
		return self.__posny
	
	def changeposn(self,newx, newy):
		self.__posnx = newx
		self.__posny = newy

	def getPosition(self):
		return self.__posnx,self.__posny

	def getName(self):
		return self.__name

class Player(Person):
	def __init__(self, name, posnx, posny,maxcol,level,score):
		Person.__init__(self, name, posnx, posny)
		self.score = score
		self.life = 3
		self.level = level
		self.updown = 0		#Used in implementing the spacebar jumps
		self.maxcol = maxcol
	
	def levelchange(self, newlevel):
		self.level = newlevel

	def lifechange(self, newlife):
		self.life = newlife

	def collectCoin(self):
		self.score += 5	

	def checkCollision(self,R,C):
		self.score -= 25
		self.life -= 1
		self.changeposn(R,C)
	
	def checkWall(self,xcor,ycor,arr):		
		if arr[xcor][ycor] == (-1):
			return True
		else: 
			return False	
	
	def PrincessRescued(self,R,C):
		self.score += 50
		self.love += 1
		self.changeposn(R,C)

	def getLevel(self):
		return self.level

	def getScore(self):
		return self.score

	def getLife(self):
		return self.life	

class Donkey(Person):	
	def __init__(self, name, limitleft, limitright, floornum, COL, array):		#name can be used in the case of multiple donkeys
		Person.__init__(self, name, floornum - 1, limitleft)
		
		self.limitleft = limitleft
		self.limitright = limitright
		self.direction = 1	#1 for right 2 for left
		self.qarr = []
		self.maxcol = COL
		array[self.getX()][self.getY()] = 5

	def getdir(self):
		return self.direction

	def changedir(self):
		if self.direction == 1:
			self.direction = 2
		else:
			self.direction = 1
	
	def donkeyWalk(self,array):	#Donkey walks along the floor and is implemented in this function
		if self.direction == 1: 
			if len(self.qarr) > 0:
				array[self.getX()][self.getY()] = (self.qarr).pop()
			else:
				array[self.getX()][self.getY()] = 0
			if array[self.getX()][(self.getY()+1)%self.maxcol] == 2 or array[self.getX()][(self.getY()+1)%self.maxcol] == 3 or \
				array[self.getX()][(self.getY()+1)%self.maxcol] == -1:
				(self.qarr).append(array[self.getX()][(self.getY()+1)%self.maxcol])
			self.changeposn(self.getX(),(self.getY() + 1)%self.maxcol)
			array[self.getX()][self.getY()] = 5
			if ((self.getY() + 1)%self.maxcol) == self.limitright:
				self.changedir()
		if self.direction == 2: 
			if len((self.qarr)) > 0:
				array[self.getX()][self.getY()] = (self.qarr).pop()
			else:
				array[self.getX()][self.getY()] = 0
			if array[self.getX()][(self.getY()-1+self.maxcol)%self.maxcol] == 2 or array[self.getX()][(self.getY()-1+self.maxcol)%self.maxcol] == 3 or \
				array[self.getX()][(self.getY()-1)%self.maxcol] == -1:
				(self.qarr).append(array[self.getX()][(self.getY()-1+self.maxcol)%self.maxcol])
			self.changeposn(self.getX(), (self.getY()-1+self.maxcol)%self.maxcol)
			array[self.getX()][self.getY()] = 5
			if ((self.getY() - 1 + self.maxcol)%self.maxcol) == self.limitleft:
				self.changedir()			


	def checkCollision(self,array):		#Checks collision of donkey with the player in which case the donkey dies
		if array[self.getX()][(self.getY()+1)%self.maxcol] == 4 or array[self.getX()][(self.getY()-1+self.maxcol)%self.maxcol] == 4:
			return True
		else:
			return False
	
	def killDonkey(self,array,P):	#Donkey dies if player collides with it
		array[self.getX()][self.getY()+1] = 0
		array[self.getX()][self.getY()-1] = 0
		array[self.getX()][self.getY()] = 0
		tempx,tempy = P.getPosition()
		P.changeposn(tempx,tempy)
		array[tempx][tempy] = 4
		

class Fireball:
	def __init__(self, posnx, posny, array, direction):
		self.__posnx = posnx
		self.__posny = posny
		if direction == 1:
			self.direction = 2
		else:
			self.direction = 1	#1 for right 2 for left
		self.miscarr = []
		array[self.__posnx][self.__posny] = 6
		self.larray = []		

	def checkwall(self, xcor, ycor, array):		#Checks if fireball has hit the wall
		if self.direction == 1:
			if array[xcor][(ycor + 1)%80] == (-1):
				return True
			else:
				return False
		else:
			if array[xcor][(ycor - 1+80)%80] == (-1):
				return True
			else:
				return False
	
	def autoPath(self, array):	#The fireball's automatic path is implemented in this function
		if self.direction == 1:
			if self.checkwall(self.__posnx,self.__posny,array) == False:
				if len((self.miscarr)) > 0:
					array[self.__posnx][self.__posny] = (self.miscarr).pop()
				else:
					array[self.__posnx][self.__posny] = 0
				if array[self.__posnx][self.__posny+1] == 2 or array[self.__posnx][self.__posny+1] == 3 or \
				array[self.__posnx][self.__posny+1] == 5:
					(self.miscarr).append(array[self.__posnx][self.__posny+1])
				self.__posny += 1
				array[self.__posnx][self.__posny] = 6
			else:
				self.direction = 2
		else:	
			if self.checkwall(self.__posnx,self.__posny,array) == False:
				if len((self.miscarr)) > 0:
					array[self.__posnx][self.__posny] = (self.miscarr).pop()
				else:
					array[self.__posnx][self.__posny] = 0
				if array[self.__posnx][self.__posny-1] == 2 or array[self.__posnx][self.__posny-1] == 3 or \
				array[self.__posnx][self.__posny-1] == 5:
					(self.miscarr).append(array[self.__posnx][self.__posny-1])
				self.__posny -= 1
				array[self.__posnx][self.__posny] = 6
			else:
				self.direction = 1
	#These functions are necessary as class Fireball doesn't inherit from Person		
	
	def getPosition(self):		
		return self.__posnx,self.__posny
	
	def getX(self):
		return self.__posnx
	
	def getY(self):
		return self.__posny

	def getDirection(self):
		return self.direction
	
	def changeposn(self,newx,newy):
		self.__posnx = newx
		self.__posny = newy
	
