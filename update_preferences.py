from google.appengine.ext import ndb

class Preferences(ndb.Model):
  name = ndb.StringProperty()
  min_5 = ndb.IntegerProperty()
  min_3 = ndb.IntegerProperty()
  min_blitz = ndb.IntegerProperty()

def write_preferences(min_5, min_3, min_blitz):
  preferences = Preferences.query(Preferences.name == 'Main Preferences').fetch()
  if preferences:
    preferences = preferences[0]
  else:
    preferences = Preferences()
    preferences.name = 'Main Preferences'
  preferences.min_5 = min_5
  preferences.min_3 = min_3
  preferences.min_blitz = min_blitz
  preferences.put()
