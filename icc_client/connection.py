# Template from Ryan Chiu. See https://code.google.com/p/ics-bot-maker/

import socket
import sms
import sys
import datetime

class Connection:

  def __init__(self, server_host, server_port, server_prompt,
               username, password, buffer_size, preferences):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.buffer_size = buffer_size        
    self.server_host = server_host
    self.server_port = server_port
    self.server_prompt = server_prompt
    self.username = username
    self.password = password.password
    self.preferences = preferences
    self.sock.connect((self.server_host, self.server_port))
    
  def connect(self, listening=False):
    # Print data until server prompts for a username, in which case it
    # will be entered.
    self.read_until('login: ')
    self.write_line(self.username)

    # Ditto for the password
    self.read_until('password: ')
    self.write_line(self.password)

    curr_time = datetime.datetime.utcnow()
        
    #If almost 10 minutes have passed, close the connection.
    while (datetime.datetime.utcnow() - curr_time).seconds < 590:
      line = self.read_line()
      if line and listening:
         self.process_line(line.strip())

    print("10 minutes have passed, connection closed")
    self.sock.close()

  def process_line(self, line):
    if line.startswith('Game notification:'):
      self.handle_game_notification(line)

  #If the game notification is of high enough interest, send an SMS.
  def handle_game_notification(self, notification):
    tokens = notification.rsplit(' ')
    player1 = tokens[2]
    player1_rating = int(tokens[3].strip('()'))
    player2 = tokens[5]
    player2_rating = int(tokens[6].strip('()'))
    time_control = tokens[8]
    players = [player1.lower(), player2.lower()]
    key_players = ['capilanobridge', 'adaptation', 'depressnyak',
      'velimirovich', 'rafaello', 'dsquared', 'azerichess',
      'mlraka', 'egor-geroev2']

    for player in key_players:
      if player in players:
        self.send_message('%s is playing' % player)
        return

    if time_control == '3-minute':
      if (player1_rating + player2_rating > self.preferences.min_3 or
          max(player1_rating, player2_rating) > 2700):
        self.send_message('3min game between %s (%s) and %s (%s)' % (
          player1, player1_rating, player2, player2_rating))

    elif time_control == '5-minute':
      if (player1_rating + player2_rating > self.preferences.min_5 or
          max(player1_rating, player2_rating) > 2800):      
        self.send_message('5min game between %s (%s) and %s (%s)' % (
          player1, player1_rating, player2, player2_rating))

    elif time_control == 'blitz':
      if player1_rating + player2_rating > self.preferences.min_blitz:
        self.send_message('Blitz game between %s (%s) and %s (%s)' % (
          player1, player1_rating, player2, player2_rating))

  def send_message(self, message):
    SMS = sms.SMS()
    SMS.send_sms(message)

  #Select doesn't work on GAE.
  def read_line(self):
    try:
      recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
    except:
      return None
    print recv
    return recv
    '''
    readlist, _, _ = select([self.sock, sys.stdin], [], [])
    for sock in readlist:
      if sock == sys.stdin:
        command = sys.stdin.readline()
        self.write_line(command)
        print('Sending command: %s' % command)
      if sock == self.sock:
        recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        print recv
        return recv
    '''
  def read_until(self, end_str):
    recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
    while end_str not in str(recv):
      print recv

  def write_line(self, str):
    str += "\n"
    self.sock.send(str)

  # Some getter/setter methods that I thought might be necessary
  def get_server_host(self): return self.server_host
  def get_server_prompt(self): return self.server_prompt
  def get_server_port(self): return self.server_port
  def is_connected(self): return self.connected
  def is_connecting(self): return self.connecting  
  def set_server_host(self, host): self.server_host = host
  def set_server_prompt(self, prompt): self.server_prompt = prompt
  def set_server_port(self, port): self.server_port = port
