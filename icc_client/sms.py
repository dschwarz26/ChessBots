# Class for sending SMS messages.

#from google.appengine.api import mail
import logging
import utils
import sendgrid

class SMS:
  
  def __init__(self):
    self.email = 'danielschwarz26@gmail.com'
    password = utils.Password.query(
      utils.Password.name == 'sendgrid_password').fetch()[0].password
    self.sg = sendgrid.SendGridClient('dschwarz26', password)

  #Works only for T-Mobile phones.
  def send_sms(self, phone_number, text):
    #recipient = phone_number + '@tmomail.net' # self.email
    recipient = 'danielschwarz26@gmail.com'
    message = sendgrid.Mail(
      to=recipient,
      subject='ICC Notification',
      text=text,
      from_email='danielschwarz27@gmail.com')
    status, msg = self.sg.send(message)
    logging.debug('Sent message %s to address %s. Status %s %s' % (
        text, recipient, msg, status))
    #mail.send_mail(
    #    self.email,
    #    phone_number + '@tmomail.net',
    #    'ICC Notification!',
    #    message
    #)
   # logging.info('Sent')
