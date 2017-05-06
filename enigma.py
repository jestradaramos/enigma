# This will be the start of my enigma simulator
# I will need
# 	- Plug switch simulator
#	- CogWheel
# 	- Light up of keys

## This file will be for the componenets of the enigma machine

class PlugBoard():
	def __init__(self,settings):
		# Here we are expecting 10 pairs of letters separated by commas
		# We will assumer there are no replicas
		self.forward = {}
		split = settings.split(',')
		for x in split:
			self.forward.update({x[0] : x[1]})
		self.backward = {v: k for k,v in self.forward.items()}
		

	def goForward(self, forward):
		return self.forward[forward]
	
	def goBackward(self, reverse):
		return self.backward[reverse]


# These are just testing the functionality of the cogwheel
x = PlugBoard("A1,B2,C3")
print (x.forward)
print (x.backward)
print (x.goForward('A'))

class CogWheel():
	def __init__(self,discNum ,settings):
		# Here we expect a list of pair of letter, A-Z
		# First letter of each pair should follow alphabetical order
		# Ex. AZ,BF,CD,DR[edit: dnt matter, just needs all letters paired]
		split = settings.split()
		self.forward = []
		self.backward = []
		for x in split():
			self.forward.append(ord(x[0]) - 65)
			self.backward.append(ord(x[1]) - 65)
		self.ind = 0
		self.discNum = discNum

	def goForward(self, ind):
		value = self.forward[ind]
		return self.backward.index(value)

	def goBackward(self, ind):
		value = self.backward[ind]
		return self.forward[value]
	
	def rotate(self):
		tempF = []
		tempB = []
		for x in range(1,len(self.forward)):
			tempF.append(self.forward[x])
			tempB.append(self.backward[x])

		tempF.append(self.forward[0])
		tempB.append(self.backward[0])

		self.forward = tempF
		self.backward = tempB

	
	def set(self, setting):
		tempF = []
		tempB = []
		for x in range(setting,len(self.forward)):
			tempF.append(self.forward[x])
			tempB.append(self.backward[x])

		for x in range(0,setting):
			tempF.append(self.forward[x])
			tempB.append(self.backward[x])

		self.forward = tempF
		self.backward = tempB
		

	


