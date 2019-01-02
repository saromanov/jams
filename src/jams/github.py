from github import Github

class GithubProvider(Provider):
    def __init__(self, token):
        Provider.__init__(self, token)