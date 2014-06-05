import random



DATA =[]


def reload():
	global DATA
	DATA = [[True,True,True,False,False],[True,True,False,False,True],[True,False,False,True,False],[False,False,False,True,True],[True,False,False,True,False],[False,False,False,True,True]]

	#for line in open("cols.txt"):
	#	DATA.append(list(line[:len(line)-1]))

	



class X:
	weights=[]

	def __init__(self):
		self.weights = [1,2,1,2,1,2]
		"""for line in open("w1.txt"):
			wei=line.split()
		self.weights = [int(cy) for cy in wei]
		#print weights
		"""

		print len(DATA[0])
		print len(self.weights)


	#for line in open("w1.txt"):
	#	wei=line.split()
	#weights = [int(cy) for cy in wei]

	def checkrowcover(self,columns):

		if len(columns)==1:
			return all(columns[0])


		retlist=[False for x in columns[0]]
		#print retlist
		colno=0
		itemno=0
		for col in columns:
			itemno=0
			#print "---"
			for item in col:
				if item == True: 
					#print itemno
					retlist[itemno]=True
				itemno+=1

		#print retlist

		return all(retlist)

	def calcCost(self,res):
		cost =0
		#print res
		for ele in res:
			cost = cost + self.weights[ele]

		return cost


	def findSolution(self):
		global DATA
		reload()
		copyData=DATA[:]
		#copyweights=self.weights[:]
		eIdx=0
		rweight=[]
		rele=[]


		res=[]
		xvar=-1

		#print copyData

		for i in range(len(copyData)):

			xvar = -1
			while (xvar == -1 ):
				if all(v==-1 for v in copyData)==True:
					break

				eIdx=random.randrange(len(copyData))
				xvar = copyData[eIdx]

			rele.append(copyData[eIdx])

			copyData[eIdx]=-1
			res.append(eIdx)

			if self.checkrowcover(rele) == True:
				reload()
				return list(set(res));

		reload()
		res=list(set(res))


		#print res


		return res


	def DO(self):
		global DATA

		solution = self.findSolution()
		xCost = self.calcCost(solution)
		reload()

		#print solution

		for nIdx in range(int(0.8 * len(DATA))):
			

			tsolution = self.findSolution()

			#print "\nCalculated solution for Attempt " + str(nIdx+1) +" = " + str(tsolution)

			reload()

			tcost = self.calcCost(tsolution)

			#print "\nCalculated cost for Attempt " + str(nIdx+1) +" = " + str(tcost)


			if tcost<xCost:
				solution=tsolution
				xCost=tcost
			#else : 
			#	"Not change is solution"

		return solution,xCost
		#print xCost
		#print self.calcCost(res)




reload()
var=X()

#print var.checkrowcover([[True,True,True,True,False],[True,True,False,True,False]])

print "input values represented as Trues instead of 1's:"
print DATA

print "weights for each column:"
print var.weights

s,v= var.DO()

print "optimal vertex cover rows indexes for given input is "
print s 
print "and its cost is"
print v