# Class for sending SMS messages.

from google.appengine.api import mail
import logging

class SMS:
  def __init__(self):
    self.email = 'danielschwarz26@gmail.com'

  #Works only for T-Mobile phones.
  def send_sms(self, message, phone_number):
    mail.send_mail(
        self.email,
        phone_number + '@tmomail.net',
        'ICC Notification!',
        message
    )
    logging.info('Sent')
