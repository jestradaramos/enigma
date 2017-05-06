import smtplib

class email():
	
	def __init__(self):
		self.email = "jestrada321@gmail.com"
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(self.email, "JE20179chs")
 
	def send(self, to, msg):
		self.server.sendmail(self.email, to, msg)
		self.server.quit()



x = email()
x.send("6179906639@vtext.com", "test")
