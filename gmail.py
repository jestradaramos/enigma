import smtplib

class email():
	
	def __init__(self):
		self.email = input("Insert email: ")
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(self.email, input("Insert Password"))
 
	def send(self, to, msg):
		self.server.sendmail(self.email, to, msg)
		self.server.quit()



x = email()
x.send("6179906639@vtext.com", "test")
