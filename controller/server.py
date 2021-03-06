import json

from google.appengine.api import users

import webapp2

from controller.connectors import RealDebridServiceConnector
from model import queries
from environment import JINJA_ENVIRONMENT, REAL_DEBRID_CREDENTIALS, FILE_STORE_LIMIT


class MainPage(webapp2.RedirectHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            template = JINJA_ENVIRONMENT.get_template('index.html')
            self.response.write(template.render({'user': user}))
        else:
            self.redirect(users.create_login_url(self.request.uri))


class Unrestrictor(webapp2.RedirectHandler):

    def post(self):
        user = users.get_current_user()
        data = self.request.body
        data = json.loads(data)
        c = RealDebridServiceConnector(**REAL_DEBRID_CREDENTIALS)
        f = c.unlock_link(data["url"])
        if not isinstance(f, dict):
            ret = {
                'unrestrictedUrl': f.unrestricted_url
            }
            f.user = user
            f.put()
            files = queries.get_files_for_user(user)
            if len(files) > FILE_STORE_LIMIT:
                files[-1].key.delete()
            f = ret
        else:
            self.response.set_status(500)
        self.response.write(json.dumps(f))


class Archiver(webapp2.RedirectHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            files = queries.get_files_for_user(user)
            ret = []
            for f in files:
                ret.append({
                    'unrestrictedUrl': f.unrestricted_url,
                    'filename': f.filename,
                    'sourceUrl': f.source_url
                })
            self.response.write(json.dumps(ret))
        else:
            self.redirect(users.create_login_url(self.request.uri))