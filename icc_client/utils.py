# Helpful things.
from google.appengine.ext import ndb
import logging

class Password(ndb.Model):
  name = ndb.StringProperty()
  password = ndb.StringProperty()

class User(ndb.Model):
  name = ndb.StringProperty()
  phone_number = ndb.StringProperty()
  # Each category is a dictionary that has a minimum combined
  # rating for each given time period.
  min_5 = ndb.IntegerProperty(repeated=True)
  min_3 = ndb.IntegerProperty(repeated=True)
  min_blitz = ndb.IntegerProperty(repeated=True)

def update_user(name, morning, afternoon, evening):
  try:
    user = User.query(User.name == name).fetch()[0]
  except:
    logging.error('Unable to retrieve player %s' % name)
  else:
    min_5_values = [0] * 24
    min_3_values = [0] * 24
    min_blitz_values = [0] * 24
    for i in range(1, 7):
      min_5_values[i] = 5400
      min_3_values[i] = 5200
      min_blitz_values[i] = 6800
    for i in range(7, 10):
      min_5_values[i] = morning['min_5']
      min_3_values[i] = morning['min_3']
      min_blitz_values[i] = morning['min_blitz']
    for i in range(10, 19):
      min_5_values[i] = afternoon['min_5']
      min_3_values[i] = afternoon['min_3']
      min_blitz_values[i] = afternoon['min_blitz']
    for i in range(19, 24) + [0]:
      min_5_values[i] = evening['min_5']
      min_3_values[i] = evening['min_3']
      min_blitz_values[i] = evening['min_blitz']
    user.min_5 = [int(val) for val in min_5_values]
    user.min_3 = [int(val) for val in min_3_values]
    user.min_blitz = [int(val) for val in min_blitz_values]
    user.put()
    logging.info('Preferences updated for %s' % name)
