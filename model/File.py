from google.appengine.ext import ndb


class File(ndb.Model):
    """Simple container that holds the source url, the unlocked one, size, etc.

    """

    user = ndb.GenericProperty()
    source_url = ndb.StringProperty(indexed=True)
    unrestricted_url = ndb.StringProperty()
    filename = ndb.StringProperty()
    file_locker = ndb.StringProperty()
    size = ndb.IntegerProperty()
    creation_date = ndb.DateTimeProperty()