# Helpful things.
from google.appengine.ext import ndb

class Password(ndb.Model):
  name = ndb.StringProperty()
  password = ndb.StringProperty()

class User(ndb.Model):
  name = ndb.StringProperty()
  phone_number = ndb.StringProperty()
  min_5 = ndb.IntegerProperty()
  min_3 = ndb.IntegerProperty()
  min_blitz = ndb.IntegerProperty()
