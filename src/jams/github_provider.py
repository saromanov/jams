import base64
from github import Github
from provider import Provider


class GithubProvider(Provider):
    def __init__(self, token, url):
        Provider.__init__(self, token, url)
        self.client = Github(token)

    def get_repo(self, name):
        '''
            return repository by the name
        '''
        return self.client.get_repo(name)

    def get_open_issues(self, name):
        '''returns list of open issues
        '''
        repo = self.get_repo(name)
        return repo.get_issues(state='open')

    def get_content_file(self, repo, name):
        '''returns specific content file
           before return, file will be decoded via base64
        '''
        r = self.get_repo(repo)
        return base64.b64decode(r.get_contents(name).content)
