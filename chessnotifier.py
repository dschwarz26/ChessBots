import os
import webapp2
import jinja2
import cgi
import update_preferences

import main

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  template = JINJA_ENVIRONMENT.get_template('home.html')
  template_values = {}

  def get(self):
    self.response.write(self.template.render(self.template_values))

  def post(self):
    min_5 = int(cgi.escape(self.request.get('5min')))
    min_3 = int(cgi.escape(self.request.get('3min')))
    min_blitz = int(cgi.escape(self.request.get('blitz')))
    update_preferences.write_preferences(min_5, min_3, min_blitz)
    self.response.write('Preferences updated.')
    #self.response.write(self.template.render(self.template_values))

class Connection(webapp2.RequestHandler):
  
  def get(self):
    main.run()  

application = webapp2.WSGIApplication([
	('/', MainPage),
  ('/connect', Connection),
], debug = True)
