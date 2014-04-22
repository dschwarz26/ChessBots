# Class for sending SMS messages.

from google.appengine.api import mail

class SMS:
	def __init__(self):
		#self.server = smtplib.SMTP('localhost')
		self.email = 'danielschwarz26@gmail.com'
		self.phone_number = '9167170998' #utils.get_from_file('phone_number.txt')

	#Works only for AT&T phones.
	def send_sms(self, message, number=None):
		if not number:
			number = self.phone_number
		mail.send_mail(self.email, self.emailnumber.rstrip() + '@mms.att.net', '', message)
