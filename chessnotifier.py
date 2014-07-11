import os
import webapp2
import jinja2
import cgi
import main
import logging
import sendgrid
import icc_client.utils

JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):

  def read(self, name):
    return cgi.escape(self.request.get(name))

  def get(self):
    #phone_number = User.query(User.name == 'Dan').fetch()[0].phone_number
    template = JINJA_ENVIRONMENT.get_template('home.html')
    template_values = {
    #"phone_number": phone_number,
    }   
    self.response.write(template.render(template_values))

  def post(self):
    name = self.read('Name')
    morning = {
      'min_5': self.read('min_5 morning'),
      'min_3': self.read('min_3 morning'),
      'min_blitz': self.read('min_blitz morning'),
    }
    afternoon = {
      'min_5': self.read('min_5 afternoon'),
      'min_3': self.read('min_3 afternoon'),
      'min_blitz': self.read('min_blitz afternoon'),
    } 
    evening = {
      'min_5': self.read('min_5 evening'),
      'min_3': self.read('min_3 evening'),
      'min_blitz': self.read('min_blitz evening'),
    }
    logging.debug('Got an update preferences request with the following info:')
    logging.debug('Name: %s' % name)
    logging.debug(morning)
    logging.debug(afternoon)
    logging.debug(evening)
    icc_client.utils.update_user(name, morning, afternoon, evening)
    self.response.write('%s: your preferences have been updated.' % name)

class Connection(webapp2.RequestHandler):
  
  def get(self):
    main.run()  

application = webapp2.WSGIApplication([
	('/', MainPage),
  ('/connect', Connection),
], debug = True)

logging.getLogger().setLevel(logging.DEBUG)


