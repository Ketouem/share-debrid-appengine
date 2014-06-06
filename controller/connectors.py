from abc import abstractmethod
import urllib2
import urllib
import hashlib
import json

from controller.exceptions import NotConnectedError


class ServiceConnector:

    _endpoint = None

    def __init__(self, username, password):
        self._username = username
        self._password = password

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def unlock_link(self, url):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


class RealDebridServiceConnector(ServiceConnector):
    """The connector for the real-debrid service

    Attributes:
        _auth_cookie    The cookie 'auth=...' sent back by the login method
    """

    _endpoint = "https://real-debrid.com/ajax"

    def __init__(self, user, password):
        ServiceConnector.__init__(self, user, password)
        self._auth_cookie = None
        if user is not None and password is not None:
            self.connect()

    def connect(self):
        """Start a connection with real-debrid's api

        """
        login_data = urllib.urlencode({
            'user': self._username,
            'pass': hashlib.md5(self._password).hexdigest()
        })
        url = self._endpoint + '/login.php?' + login_data
        result = urllib2.urlopen(url)
        response = json.loads(result.read())
        self._auth_cookie = response["cookie"]

    def unlock_link(self, url):
        """Unrestrict a file locker link given its url

        :param url: The url of the file locker you want to un-restrict
        :type url: str
        :return: the unlocked url
        """
        if self._auth_cookie is None:
            raise NotConnectedError('No auth cookie is available.')
        else:
            api_url = self._endpoint + '/unrestrict.php?link={}'.format(url)
            opener = urllib2.build_opener()
            opener.addheaders.append(('Cookie', self._auth_cookie))
            result = opener.open(api_url)
            response = json.loads(result.read())
            return response['main_link']

    def is_connected(self):
        return self._auth_cookie is not None