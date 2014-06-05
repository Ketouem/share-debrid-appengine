import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.getcwd(), "views")),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)