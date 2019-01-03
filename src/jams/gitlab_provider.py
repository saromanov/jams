import gitlab
from provider import Provider

class GitlabProvider(Provider):
    def __init__(self, token):
        self._token = token