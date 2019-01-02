from github import Github

class GithubProvider(Provider):
    def __init__(self, token):
        Provider.__init__(self, token)
        self.client = Github(token)
    
    def get_repository(self, name):
        '''
            return repository by the name
        '''
        return self.client.get_repo(name)
    
    def get_open_issues(self, name):
        '''
            returns list of open issues
        '''
        repo = self.client.get_repo(name)
        return repo.get_issues(state='open')