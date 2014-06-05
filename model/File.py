from google.appengine.ext import ndb


class File(ndb.Model):
    """Simple container that holds the source url, the unlocked one, size, etc.

    """

    user = ndb.UserProperty()
    source_url = ndb.StringProperty(indexed=True)
    filename = ndb.StringProperty()
    file_locker = ndb.StringProperty()
    size = ndb.IntegerProperty()