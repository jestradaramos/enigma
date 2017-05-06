from gmail import *
from construct import *
# This will be where everything comes together

running = True
enigmaMachine = Machine(1,2,3)
gmail = email()

while (running):
	print("Pick an option")
	print("\t1) Encrypt/Decrypt Message")
	print("\t2) Select Rotors")
	print("\t3) Set Rotors")
	print("\t4) Set up plugboard")
	print("\t5) Send encrypted message")
	option = int(input("Option: "))
	
	if (option == 1):
		msg = input("Enter Message: ")
		encrypt = ""
		for x in msg:
			encrypt += enigmaMachine.input(x)

		print(encrypt)
		
	elif (option == 2):
		wheel = int(input("Which rotor do you want to replace?"))
		rotor = int(input("Which rotor do you want?"))
		enigmaMachine.select_cog(wheel, rotor)

		print ("New Cogwheel has been set")

	elif (option == 3):
		wheel1 = int(input("Wheel 1: "))
		wheel2 = int(input("Wheel 2: "))
		wheel3 = int(input("Wheel 3: "))

		enigmaMachine.set_up(wheel1, wheel2, wheel3)

		print ("Engima Machine has been set")
	
	elif (option == 4):
		ready = input("Make sure new plugboard is all set(y/n): ")
		while(ready != 'y'):
			ready = input()
		
		fileName = open("plugboard.txt")
		plug = fileName.read()
		enigmaMachine.set_plug(plug)
		print ("PlugBoard is all set")

	elif (option == 5):
		msg = input("Enter Message: ")
		encrypt = ""
		for x in msg:
			encrypt += enigmaMachine.input(x)
		
		message = "The following has been encrypted with the enigma machine\n"
		message += encrypt

		to = input("Insert email to send to: ")
		gmail.send(to, message)
	else:
		print("Invalid Option")
