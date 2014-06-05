from google.appengine.api import users

import webapp2


class DebridPage(webapp2.RedirectHandler):

    def get(self):
        user = users.get_current_user()

        # TODO: Add whitelisting logic