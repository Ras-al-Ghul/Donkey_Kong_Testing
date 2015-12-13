#The bonus features of the game like random floors and random stairs is implemented in this file

import random
from playerandball import Player

class Board:
	def init(self, cols, rows, array, P):	
		#Default Constructor not used as we cannot check return value easily
		#The use of default constructor was also tried, but as initializing the board is a very large function and as its return value is critical,
		#another function is being used in place of the default constructor
		
		#Initializing the board		 -1 : wall, 0 : blank, 1 : princess, 2 : stairs, 3 : coin, 4 : player, 5 : donkey, 6 : fireball
		arrwalllen=[cols-(10*3),cols-(10*3),cols-(10*2),cols-(10*1)]
		pwalllen=cols/8		
		ranges=cols/4	
		#Nothing is hardcoded	

		self.basicArray(array, rows, cols)	
	
		orgps,ps = self.princessCage(array, rows, cols ,pwalllen)
		
		global maxstairs,maxt
		maxstairs = 0
		maxstairs,step,maxt = self.levelVarSet(P)
		
		testnumofcoins = 0
		testofthree = False

		ps,ranges,arrwalllen,testnumofcoins,testofthree = self.createFandC(array, rows, cols, ps, ranges, arrwalllen, step)
		
		
		returnval = self.createStairs(array, rows, cols, ps, ranges, arrwalllen, step, pwalllen, P, orgps, maxstairs, maxt)
		if returnval == False:
			return returnval,testnumofcoins,testofthree
	
	
		#Initialize Player spawn position to the bottom left corner
		array[rows-2][1]=4
		P.changeposn((rows - 2),1)
		return True,testnumofcoins,testofthree	
		
	def basicArray(self, array, rows, cols):

		#Create basic array
    		for i in range(rows):
       			arrayRow = []
        		for j in range(cols):
		            if (i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1)):
		                arrayRow += [-1]
			    else:
				arrayRow += [0]
			array += [arrayRow]
		#Basic array created	

	def princessCage(self, array, rows, cols, pwalllen):
	
		#Create Princess cage
		ps=random.randrange(1,cols-pwalllen-2)
		array[1][ps]=-1
		array[1][ps+pwalllen]=-1
		orgps=ps+(ps%(pwalllen-1))+1
		array[1][orgps]=1
		self.princess = orgps
		for j in range(ps,ps+pwalllen+1):
			array[2][j]=-1
		return orgps,ps
		#Princess cage and Princess position is done	
	
	def levelVarSet(self, P):
		#This section changes the number of stairs and the number of coins in the game according to the level
		#In the lower level more coins are generated and in the higher levels less are generated
		#There are more paths to the princess in the lower levels
		#In the third level there exists only one path to the princess
		if P.getLevel() == 1:
			step=4
			maxstairs=2
			maxt = 10
		elif P.getLevel() == 2:
			step=7
			maxstairs=1
			maxt = 3
		else:
			step=10	
			maxstairs=0
			maxt = 3
		return maxstairs,step,maxt

	def createFandC(self, array, rows, cols, ps, ranges, arrwalllen, step):
	
		#Create floors
		#The floors are generated randomly for each board and for each level - A major challenge later on
		#Nothing is hardcoded
		testnumofcoins = 0
		tempcount=0
		self.indexarr=[]
		self.lenarr=[]
		interval = 4
		for i in range(5,rows-3,interval):
			if i != 5:
				if random.randint(0,1)==1:
					self.indexarr+=[(ps+ranges+cols)%cols]
				else:
					self.indexarr+=[(ps-ranges+cols)%cols]
			else:
				self.indexarr+=[(ps-ranges+cols)%cols]
			ps=self.indexarr[tempcount] 
			if (tempcount%2) == 0:
				self.lenarr+=[arrwalllen[random.randint(0,2)]]
			else:
				self.lenarr+=[arrwalllen[3]]
			j=0
			#Create coins
			
			k=0
			while k < (self.lenarr[tempcount]):		
				if random.randint(0,1) == 1:
					tempcol=((self.indexarr[tempcount]+k)%cols)
					if tempcol != 0 and tempcol != (cols-1):
						array[i-1][tempcol] = 3
						testnumofcoins += 1
				k+=step

			#Coins done
			while j < self.lenarr[tempcount]:
				array[i][(self.indexarr[tempcount]+j)%cols]=-1
				j+=1
			tempcount+=1
		#Ground floor coins - a special case
		k=1
		while k < (cols-1):
			if random.randint(0,1) == 1:
				array[rows-2][k] = 3
			k+=5
		#Ground floor coins done
		#Floors done
		if interval == 4:
			return ps,ranges,arrwalllen,testnumofcoins,True
		else:
			return ps,ranges,arrwalllen,testnumofcoins,False
		
	
	def chkCont(self,currrow, currcol, nextcol, arrs): 
		#This is a utility function which checks whether there exists a path from player spawn position to the princess
		#This ensures that the player is not stuck
		#It is used only while creating the board	
		if currcol < nextcol:
			currcol += 1
			while arrs[currrow][currcol] == -1 and currcol <= nextcol:
				currcol +=1 
				if currcol == nextcol:
					return True	
			return False
		else:
			currcol -= 1
			while arrs[currrow][currcol] == -1 and currcol >= nextcol:
				currcol -=1 
				if currcol == nextcol:
					return True
			return False

	def createStairs(self, array, rows, cols, ps, ranges, arrwalllen, step, pwalllen, P, orgps, maxstairs, maxt):
		#Create stairs
	
		for i in range(2,5):
			array[i][orgps]=2
	
		#The compulsary stairs ensure that there is exists path from the player spawn position to the princess
		#This is not a given as floors are generated randomly
		#Uses a kind of backtracking algorithm
		#The large number of variables are necessary		

		#Create compulsary stairs
		colnos = orgps
		rownos = 5
		colarr = [orgps]
		colarrcount = 0
		direction = 1		#1+ right 0- left
		numoftries = 0
		while rownos < (rows - 1):
			numoftries += 1
			if numoftries > 10000:
				return False			
			if direction == 1:
				tempnewcol = ((colarr[colarrcount] + (random.randint(1,5) * 10)) + cols) % cols
				if array[rownos][tempnewcol] == -1 and array[rownos + 4][tempnewcol] == -1 and self.chkCont(rownos,colarr[colarrcount],tempnewcol,array) and tempnewcol != 0 and tempnewcol != (cols-1) and tempnewcol != 1:
					rownos += 4
					colarr.append(tempnewcol)
					colarrcount += 1
					direction = random.randint(0,1)
					continue
				else:
					continue
			else: 
				tempnewcol = ((colarr[colarrcount] - (random.randint(1,5) * 10)) + cols) % cols	
				if array[rownos][tempnewcol] == -1 and array[rownos + 4][tempnewcol] == -1 and self.chkCont(rownos,colarr[colarrcount],tempnewcol,array) and tempnewcol != 0 and tempnewcol != (cols-1) and tempnewcol != 1:
					rownos += 4
					colarr.append(tempnewcol)
					colarrcount += 1
					direction = random.randint(0,1)
					continue
				else:
					continue
		
		rownos = 5
		colarrcount = 1
		while rownos < (rows - 1):
			for j in [0,1,2,3]:
				array[rownos + j][colarr[colarrcount]] = 2
			rownos += 4
			colarrcount += 1
				
		#Compulsary stairs done	
				
		#Generating random stairs and random broken stairs
		#The number of such stairs vary from level to level
		#The lower levels have more stairs while the higher levels have lesser number of stairs	
		#The large number of variables are necessary		
	
		numoft = 0
		rownos = 5
		colcount = 0
		numofs = 0
		while rownos < (rows - 1):
			floorbeg = self.indexarr[colcount]
			floorlen = self.lenarr[colcount]
			while numofs < maxstairs and numoft < maxt:
				
				tempcol = (random.randint(floorbeg,floorbeg+floorlen)+cols)%cols
				
				if (array[rownos][tempcol] == -1 and array[rownos+4][tempcol] == -1):					
					succ = 1
					tc = 1
					while tc < 10:
						if array[rownos][(tempcol+tc)%cols] == 2:
							succ = 0
						tc += 1
					tc = 1
					while tc < 10:
						if array[rownos][((tempcol-tc)+cols)%cols] == 2:
							succ = 0
						tc += 1
					if succ == 1:
						for x in [0,1,2,3]:
							if x == 2:
								if random.randint(0,1) == 1:	
									array[rownos+x][tempcol] = 2					
							else:
								array[rownos+x][tempcol] = 2
					numofs += 1
				numoft += 1
			numoft = 0
			numofs = 0
			colcount += 1
			rownos += 4			
		#Stairs done
	
	def brokenstairs(self,mainarr):
		if mainarr[1][self.princess] == 1:
			return True
		else:
			return False

	def forDonkey(self,num):
		#This function is used later in creating the Donkey
		return self.indexarr[num],self.lenarr[num]
