import argparse
import os
from gitlab_provider import GitlabProvider
from github_provider import GithubProvider
from jams import Jams

class App(object):
    def __init__(self, description, version, command_manager=None):
        self.command_manager = command_manager
        self._provider = None
        self._providers_inn = dict(github=GithubProvider, gitlab=GitlabProvider)
    
    def build(self, url):
        ''' build creates a new object
        '''
        self.jams = Jams(url, self._make_provider(self._parse_url(url)))
    
    def start(self):
        ''' starting of execution of app
        '''
        if self.jams is None:
            raise Exception("App is not initialized")
        self.jams.start()
    
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
        reading of access token from environment variable
        '''
        token = os.environ['GITHUB_TOKEN']
        if not token:
            token = os.environ['GITLAB_TOKEN']
        return self._providers_inn[provider_name](token)
