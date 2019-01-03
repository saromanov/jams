import argparse

class App(object):
    def __init__(self, description, version, command_manager):
        self.command_manager = command_manager
        self._provider = None
        self._providers_inn = dict(github=GithubProvider)
    
    def build(self, url):
        pass
    
    def _parse_url(self, url):
        if not url: raise Exception("url is not defined")
        if url.find('github.com') != -1:
            self._provider = GithubProvider()
        if url.find('gitlab.com'):
            self._provider = GitlabProvider()

    def make_provider(self, provider_name):
        '''
            initialization of provider
        '''
        self._provider = self._providers_inn[provider_name]()