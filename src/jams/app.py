import argparse
from gitlab_provider import GitlabProvider
from github_provider import GithubProvider

class App(object):
    def __init__(self, description, version, command_manager=None):
        self.command_manager = command_manager
        self._provider = None
        self._providers_inn = dict(github=GithubProvider, gitlab=GitlabProvider)
    
    def build(self, url):
        self._provider = self._make_provider(self._parse_url(url))
    
    def _parse_url(self, url):
        ''' parsing of the input url
        if url not contains github and gitlab
        then raise exception thats provider is not defined
        '''
        if not url: raise Exception("url is not defined")
        if url.find('github.com') != -1:
            return 'github'
        if url.find('gitlab.com'):
            return 'gitlab'
        raise Exception("unable to find provider")

    def _make_provider(self, provider_name):
        '''initialization of provider
        '''
        return self._providers_inn[provider_name]('')
