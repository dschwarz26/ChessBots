import os
import webapp2
import jinja2
import cgi
import update_preferences
import main
import logging
from icc_client.utils import Contact

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def get(self):
    phone_number = Contact.query(Contact.name == 'Dan').fetch()[0].phone_number
    template = JINJA_ENVIRONMENT.get_template('home.html')
    template_values = {
    "phone_number": phone_number,
    "time_windows": None, 
    }   
    self.response.write(template.render(template_values))

  def post(self):
    min_5 = int(cgi.escape(self.request.get('5min')))
    min_3 = int(cgi.escape(self.request.get('3min')))
    min_blitz = int(cgi.escape(self.request.get('blitz')))
    update_preferences.write_preferences(min_5, min_3, min_blitz)
    self.response.write('Preferences updated.')
    #self.response.write(template.render(template_values))

class Connection(webapp2.RequestHandler):
  
  def get(self):
    main.run()  

application = webapp2.WSGIApplication([
	('/', MainPage),
  ('/connect', Connection),
], debug = True)

logging.getLogger().setLevel(logging.DEBUG)


