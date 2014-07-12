import logging
import sms

from time import strftime
from utils import User

class Notifier:
  
  def __init__(self):
    self.users = User.query().fetch(10)

  def send_message(self, phone_number, message):
    SMS = sms.SMS()
    SMS.send_sms(phone_number, message)

  def handle_game_notification(self, notification):
    tokens = notification.rsplit(' ')
    player1 = tokens[2]
    player1_rating = int(tokens[3].strip('() '))
    player2 = tokens[5]
    player2_rating = int(tokens[6].strip('() '))
    time_control = tokens[8]
    players = [player1.lower(), player2.lower()]
    key_players = ['capilanobridge', 'adaptation', 'depressnyak',
      'velimirovich', 'rafaello', 'dsquared', 'azerichess',
      'mlraka', 'egor-geroev2', 'adaptation']

    hour = (int(strftime('%H')) - 7) % 24

    for user in self.users:

      for player in key_players:
        if player in players:
          self.send_message(user.phone_number, '%s is playing!' % player)
          return
      
      #self.send_message(user.phone_number, 'test')
      #logging.debug('Sent message to %s at %s' % (user.name, user.phone_number))
      if time_control == '3-minute':
        if (player1_rating + player2_rating > user.min_3[hour] or
            max(player1_rating, player2_rating) > 2700):
          self.send_message(user.phone_number, '3min game between %s (%s) and %s (%s)' % (
              player1, player1_rating, player2, player2_rating))
          logging.debug('Sent message to %s with number %s about 3min game' % (
              user.name, user.phone_number))

      elif time_control == '5-minute':
        if (player1_rating + player2_rating > user.min_5[hour] or
            max(player1_rating, player2_rating) > 2800):      
          self.send_message(user.phone_number, '5min game between %s (%s) and %s (%s)' % (
            player1, player1_rating, player2, player2_rating))
          logging.debug('Sent message to %s about 5min game' % user.name)

      elif time_control == 'blitz':
        if player1_rating + player2_rating > user.min_blitz[hour]:
          self.send_message(user.phone_number, 'Blitz game between %s (%s) and %s (%s)' % (
            player1, player1_rating, player2, player2_rating))
          logging.debug('Sent message to %s about blitz game' % user.name)


