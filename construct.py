from enigma import *


class Machine():
	def __init__(self, cog1, cog2, cog3):
		fileName = open("rotor" + str(cog1) + ".txt")
		setting1 = fileName.read()
		fileName = open("rotor" + str(cog2) + ".txt")
		setting2 = fileName.read()
		fileName = open("rotor" + str(cog3) + ".txt")
		setting3 = fileName.read()
		fileName = open("reflection.txt")
		reflection = fileName.read()
		fileName = open("plugboard.txt")
		plug = fileName.read()
		
		self.wheel1 = CogWheel(0,setting1)
		self.wheel2 = CogWheel(0,setting2)
		self.wheel3 = CogWheel(0,setting3)
		self.reflect = Reflector(reflection)
		self.board = PlugBoard(plug)
		self.count1 = 0
		self.count2 = 0

	def select_cog(self, wheel, rotor):
		fileName = open("rotor" + str(rotor) +  ".txt")

		if (wheel == 1):	
			self.wheel1 = fileName.read()
		elif (wheel == 2):
			self.wheel2 = fileName.read()
		elif (wheel == 3):
			self.wheel3 = fileName.read()
		else: 
			print("Invalid Rotor")

			
	def set_up(self, set1, set2, set3):
		self.wheel1.set(set1)
		self.wheel2.set(set2)
		self.wheel3.set(set3)

	def set_plug(self,plug):
		self.board = Plugboard(plug)

	def input(self, letter):
		string = letter.upper()
		num = ord(string) - 65

		if (num in self.board.list):
			num = self.board.list[num]

		iter1 = self.wheel1.goForward(num)
		iter2 = self.wheel2.goForward(iter1)
		iter3 = self.wheel3.goForward(iter2)
		iter4 = self.reflect.go(iter3)
		iter5 = self.wheel3.goBackward(iter4)
		iter6 = self.wheel2.goBackward(iter5)
		iter7 = self.wheel1.goBackward(iter6)

		if (iter7 in self.board.list):
			iter7 = self.board.list[iter7]
		
		final = chr(iter7 + 65)

		# TODO rotation
		self.wheel1.rotate()
		self.count1 += 1
		if (self.count1 == 26):
			self.wheel2.rotate()
			self.count2 += 1
			self.count1 = 0
		if (self.count2 == 26):
			self.wheel3.rotate()
			self.count2 = 0


		return final


print ("\n Big test")
x = Machine(1,2,3)
print (x.wheel1.backward)
print (x.wheel2.backward)
print (x.wheel3.backward)
print (x.reflect.list)
print (x.board.list)
x.set_up(3,13,24)
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))
print (x.input('A'))

