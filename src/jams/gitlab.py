import gitlab

class GitlabProvider(Provider):
    def __init__(self, token):
        self._token = token