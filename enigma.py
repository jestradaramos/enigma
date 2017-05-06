# This will be the start of my enigma simulator
# I will need
# 	- Plug Board
#	- CogWheel
# 	- Reflextion

## This file will be for the componenets of the enigma machine

class PlugBoard():
	def __init__(self,settings):
		# Here we are expecting 10 pairs of letters separated by commas
		# We will assumer there are no replicas
		self.list = {}
		split = settings.split(',')
		for x in split:
			self.list.update({ord(x[0]) - 65 : ord(x[1]) - 65})
			self.list.update({ord(x[1]) - 65 : ord(x[0]) - 65})
		

	def go(self, value):
		return self.list[value]
	
class CogWheel():
	def __init__(self,discNum ,settings):
		# Here we expect a list of pair of letter, A-Z
		# First letter of each pair should follow alphabetical order
		# Ex. AZ,BF,CD,DR[edit: dnt matter, just needs all letters paired]
		split = settings.split(',')
		self.forward = []
		self.backward = []
		for x in split:
			self.forward.append(ord(x[0]) - 65)
			self.backward.append(ord(x[1]) - 65)
		self.index = 0

	def goForward(self, ind):
		value = self.forward[ind]
		return self.backward.index(value)

	def goBackward(self, ind):
		value = self.backward[ind]
		return self.forward.index(value)
	
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
		self.index += 1

	
	def set(self, setting):
		tempF = []
		tempB = []
		start = self.forward.index(setting)
		for x in range(start,len(self.forward)):
			tempF.append(self.forward[x])
			tempB.append(self.backward[x])

		for x in range(0,start):
			tempF.append(self.forward[x])
			tempB.append(self.backward[x])

		self.forward = tempF
		self.backward = tempB
		self.index = setting
		
# It is the same as the plugboard

class Reflector():
	def __init__(self,settings):
		# Here we are expecting 13 pairs of letters separated by commas
		# We will assumer there are no replicas
		self.list = {}
		split = settings.split(',')
		for x in split:
			self.list.update({ord(x[0]) - 65 : ord(x[1]) - 65})
			self.list.update({ord(x[1]) - 65 : ord(x[0]) - 65})
		

	def go(self, value):
		return self.list[value]
