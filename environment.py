import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "views")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

REAL_DEBRID_CREDENTIALS = {
    'user': None,
    'password': None
}

FILE_STORE_LIMIT = 10

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/36.0.1944.0 Safari/537.36"