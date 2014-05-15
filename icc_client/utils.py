# Helpful things.
from google.appengine.ext import ndb

class Password(ndb.Model):
  name = ndb.StringProperty()
  password = ndb.StringProperty()

class Contact(ndb.Model):
  name = ndb.StringProperty()
  phone_number = ndb.StringProperty()
