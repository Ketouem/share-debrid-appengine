import json

from google.appengine.api import users

import webapp2

from controller.connectors import RealDebridServiceConnector
from environment import JINJA_ENVIRONMENT, REAL_DEBRID_CREDENTIALS


class MainPage(webapp2.RedirectHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            # TODO: Add whitelisting logic
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))


class Unrestrictor(webapp2.RedirectHandler):

    def post(self):
        data = self.request.body
        data = json.loads(data)
        c = RealDebridServiceConnector(**REAL_DEBRID_CREDENTIALS)
        f = c.unlock_link(data["url"])
        ret = {
            'unrestrictedUrl': f
        }
        self.response.write(json.dumps(ret))