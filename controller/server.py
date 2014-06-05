from google.appengine.api import users

import webapp2

from environment import JINJA_ENVIRONMENT


class DebridPage(webapp2.RedirectHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            # TODO: Add whitelisting logic
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.write(template.render())
        else:
            self.redirect(users.create_login_url(self.request.uri))