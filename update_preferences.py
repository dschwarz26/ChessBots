from google.appengine.ext import ndb
from icc_client.utils import User
import logging

def write_preferences(name, min_5, min_3, min_blitz):
  try:
    user = User.query(User.name == name).fetch()[0]
    user.min_5 = min_5
    user.min_3 = min_3
    user.min_blitz = min_blitz
    user.put()

  except IndexError:
    logging.error('Tried to update preferences for unknown user: %s' % name)
  
