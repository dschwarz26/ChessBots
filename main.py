#!/usr/bin/env python
# Template from Ryan Chiu.  See https://code.google.com/p/ics-bot-maker/
from icc_client import connection, utils

def run():
  # Important configuration variables for bot. Change these to fit
  # your bot's user information
  LOGIN_CONFIG = {"server_host": "chessclub.com",
                  "server_port": 5000,
                  "server_prompt": "aics%",
                  "username": "ddpbot",
                  "password": utils.Password.query(
                    utils.Password.name == 'icc_password').fetch()[0],
                  "buffer_size": 4096,
                 }
  
  # Set up connection using LOGIN_CONFIG dictionary values
  conn = connection.Connection(LOGIN_CONFIG["server_host"],
                                   LOGIN_CONFIG["server_port"],
                                   LOGIN_CONFIG["server_prompt"],
                                   LOGIN_CONFIG["username"],
                                   LOGIN_CONFIG["password"],
                                   LOGIN_CONFIG["buffer_size"])
  conn.connect(listening=True)
  
if __name__ == '__main__':
   run()
