import os
import webapp2
import jinja2
import cgi
import update_preferences
import main
import logging
from icc_client.utils import User

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def get(self):
    phone_number = User.query(User.name == 'Dan').fetch()[0].phone_number
    template = JINJA_ENVIRONMENT.get_template('home.html')
    template_values = {
    "phone_number": phone_number,
    "time_windows": None, 
    }   
    self.response.write(template.render(template_values))

  def post(self):
    name = cgi.escape(self.request.get('Name'))
    min_5 = int(cgi.escape(self.request.get('5min')))
    min_3 = int(cgi.escape(self.request.get('3min')))
    min_blitz = int(cgi.escape(self.request.get('blitz')))
    logging.info('Got an update preferences request with the following info:')
    logging.info('Name: %s' % name)
    logging.info('min_5: %d, min_3: %d, min_blitz: %d' % (min_5, min_3, min_blitz))
    update_preferences.write_preferences(name, min_5, min_3, min_blitz)
    self.response.write('%s: your preferences have been updated.' % name)
    #self.response.write(template.render(template_values))

class Connection(webapp2.RequestHandler):
  
  def get(self):
    main.run()  

application = webapp2.WSGIApplication([
	('/', MainPage),
  ('/connect', Connection),
], debug = True)

logging.getLogger().setLevel(logging.DEBUG)


