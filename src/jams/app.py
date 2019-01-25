import argparse
import os
from gitlab_provider import GitlabProvider
from github_provider import GithubProvider
from jams import Jams
import urllib.parse as urllib

class App(object):
    def __init__(self, description, version, command_manager=None):
        self.command_manager = command_manager
        self._provider = None
        self._description = description
        self._providers_inn = dict(github=GithubProvider, gitlab=GitlabProvider)
    
    def build(self, url):
        ''' build creates a new object
        '''
        url = self._parse_url(url)
        provider = self._make_provider(url.hostname.split('.')[0])
        path = url.path[1:]
        self.jams = Jams(path, provider)
    
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
        return urllib.urlparse(url)

    def _make_provider(self, provider_name):
        '''initialization of provider
        reading of access token from environment variable
        '''
        token = os.environ['GITHUB_TOKEN']
        if not token:
            token = os.environ['GITLAB_TOKEN']
        return self._providers_inn[provider_name](token)

def output(message, passed):
    '''
    output provides response for checker
    '''
    line = '[+]'
    if not passed: line = '[x]'
    print('{0}:{1}'.format(line, message))

a = App('sss', '0.1')
a.build('https://github.com/saromanov/godownload')
a.start()
