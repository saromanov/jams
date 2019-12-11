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
        self._providers_inn = dict(
            github=GithubProvider, gitlab=GitlabProvider)

    def build(self, url):
        ''' build creates a new object
        '''
        url = self._parse_url(url)
        if not url.hostname:
            raise Exception('Hostname is not defined')
        if len(url.path) == 0:
            raise Exception('Url path is not defined')
        provider = self._make_provider(url.hostname.split('.')[0], url.path[1:])
        path = url.path[1:]
        return Jams(path, provider)

    def _parse_url(self, url):
        ''' parsing of the input url
        if url not contains github and gitlab
        then raise exception thats provider is not defined
        '''
        if not url:
            raise Exception("url is not defined")
        return urllib.urlparse(url)

    def _make_provider(self, provider_name, url):
        """initialization of provider
        reading of access token from environment variable
        """
        token = os.environ['GITHUB_TOKEN']
        if not token:
            token = os.environ['GITLAB_TOKEN']
        return self._providers_inn[provider_name](token, url)


a = App('sss', '0.1')
a.build('https://github.com/saromanov/godownload').report()
