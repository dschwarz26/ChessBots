# Helpful things.
from google.appengine.ext import ndb

class Password(ndb.Model):
  name = ndb.StringProperty()
  password = ndb.StringProperty()

def run(pswd):
  password = Password()
  password.name = "icc_password"
  password.password = pswd
  password.put()

