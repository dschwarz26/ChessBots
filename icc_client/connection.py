# Template from Ryan Chiu. See https://code.google.com/p/ics-bot-maker/

import logging
import socket
import sys
import datetime
from notification import Notifier

from google.appengine import runtime

class Connection:

  def __init__(self, server_host, server_port, server_prompt,
               username, password, buffer_size):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.settimeout(300)
    self.buffer_size = buffer_size        
    self.server_host = server_host
    self.server_port = server_port
    self.server_prompt = server_prompt
    self.username = username
    self.password = password.password
    self.sock.connect((self.server_host, self.server_port))
    self.notifier = Notifier()

  def connect(self, listening=False):
    # Print data until server prompts for a username, in which case it
    # will be entered.
    self.read_until('login: ')
    self.write_line(self.username)

    # Ditto for the password
    self.read_until('password: ')
    self.write_line(self.password)

    curr_time = datetime.datetime.utcnow()
    
    self.write_line('tell danieldelpaso hi! %s' % datetime.datetime.utcnow())
    
    logging.debug('Connected!')    

    #If almost 60 minutes have passed, close the connection.
    while (datetime.datetime.utcnow() - curr_time).seconds < 3540:
      try:  
        line = self.read_line()
        if line and listening:
          logging.info(line)
          self.process_line(line.strip())
      except runtime.DeadlineExceededError:
        logging.debug('Deadline Exceeded Error')

    logging.debug("59 minutes have passed, connection restarting")

  def process_line(self, line):
    if line.startswith('Game notification:'):
      self.notifier.handle_game_notification(line)

  #Select doesn't work on GAE.
  def read_line(self):
    try:
      recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
    except:
      logging.debug('Failed to read line.')
      return None
    return recv
    '''
    readlist, _, _ = select([self.sock, sys.stdin], [], [])
    for sock in readlist:
      if sock == sys.stdin:
        command = sys.stdin.readline()
        self.write_line(command)
        logging.info('Sending command: %s' % command)
      if sock == self.sock:
        recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
        logging.info(recv)
        return recv
    '''

  def read_until(self, end_str):
    recv = self.sock.recv(self.buffer_size).replace(self.server_prompt, "")
    while end_str not in str(recv):
      logging.info(recv)

  def write_line(self, str):
    str += "\n"
    self.sock.send(str)
 
