from github import Github

class GithubProvider(Provider):
    def __init__(self, token):
        Provider.__init__(self, token)
        self.client = Github(token)
    
    def get_repository(self, name):
        repo = self.client.get_repo(name)
        print(repo)