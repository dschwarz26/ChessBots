# Class for sending SMS messages.

import smtplib
import utils

class SMS:
	def __init__(self):
		self.server = smtplib.SMTP('localhost')
		#self.server.starttls()
		self.email = 'danielschwarz26@gmail.com'
		#self.password = utils.get_from_file('gmail_password.txt')
		self.phone_number = utils.get_from_file('phone_number.txt')
		#self.server.login(self.email, self.password)

	#Works only for AT&T phones.
	def send_sms(self, message, number=None):
		if not number:
			number = self.phone_number
		self.server.sendmail(self.email, number.rstrip() + '@mms.att.net', message)

if __name__ == '__main__':
	sms = SMS()
	sms.send_sms('Blitz\: bob(1) vs bob2(1)')
	sms.send_sms('Blitz bob(3) vs bob2(4)')
	sms.send_sms('Blitz\: %s(%s) vs %s(%s)' % ('a', 1, 'b', 2))
	sms.send_sms('Blitz\: %s(%d) vs %s(%d)' % ('a', 3, 'b', 4))
	print('Sent test message to %s' % sms.phone_number)
