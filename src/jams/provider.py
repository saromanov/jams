
class Provider:
    def __init__(self, token, url):
        self._token = token
        self._url = url

    def token(self):
        return self._token

    def get_repository(self, name):
        pass

    def get_open_issues(self):
        pass
