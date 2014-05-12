# Class for sending SMS messages.

from google.appengine.api import mail

class SMS:
	def __init__(self):
		self.email = 'danielschwarz26@gmail.com'
		self.phone_number = '9167170998'

	#Works only for T-Mobile phones.
	def send_sms(self, message, number=None):
		if not number:
			number = self.phone_number
		mail.send_mail(
        self.email,
        self.phone_number + '@tmomail.net',
        'ICC Notification!',
        message
    )
