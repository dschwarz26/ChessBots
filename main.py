#!/usr/bin/env python
# Template from Ryan Chiu.  See https://code.google.com/p/ics-bot-maker/
from update_preferences import Preferences
from icc_client import connection, utils

def run():
  # Important configuration variables for bot. Change these to fit
  # your bot's user information
  LOGIN_CONFIG = {"server_host": "chessclub.com",
                  "server_port": 5000,
                  "server_prompt": "fics%",
                  "username": "ddpbot",
                  "password": utils.Password.query(
                    utils.Password.name == 'icc_password').fetch()[0],
                  "buffer_size": 4096,
                  "preferences": Preferences.query(
                    Preferences.name == 'Main Preferences').fetch()[0]
                 }
  
  # Set up connection using LOGIN_CONFIG dictionary values
  conn = connection.Connection(LOGIN_CONFIG["server_host"],
                                   LOGIN_CONFIG["server_port"],
                                   LOGIN_CONFIG["server_prompt"],
                                   LOGIN_CONFIG["username"],
                                   LOGIN_CONFIG["password"],
                                   LOGIN_CONFIG["buffer_size"],
                                   LOGIN_CONFIG["preferences"])
  conn.connect(listening=True)
  
if __name__ == '__main__':
   run()
