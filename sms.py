# Class for sending SMS messages.

import smtplib
import utils

class SMS:
	def __init__(self):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.email = 'danielschwarz26@gmail.com'
		self.password = utils.get_from_file('gmail_password.txt')
		self.phone_number = utils.get_from_file('phone_number.txt')
		self.server.login(self.email, self.password)

	#Works only for AT&T phones.
	def send_sms(self, message, number=None):
		if not number:
			number = self.phone_number
		self.server.sendmail(self.email, number.rstrip() + '@mms.att.net', message)
