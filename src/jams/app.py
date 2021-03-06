import os
from github_provider import GithubProvider
from jams import Jams
import urllib.parse as urllib


class App(object):
    def __init__(self, description, version, command_manager=None):
        self.command_manager = command_manager
        self._provider = None
        self._checkers = []
        self._config = {}
        self._description = description
        self._providers_inn = dict(
            github=GithubProvider)

    def add_checkers_from_config(self, checkers):
        '''
        adding checkers manually
        '''
        self._config = checkers

    def build(self, url):
        ''' build creates a new object
        '''
        url = self._parse_url(url)
        if not url.hostname:
            raise InputError('Hostname is not defined')
        if len(url.path) == 0:
            raise InputError('Url path is not defined')
        path = url.path[1:]
        provider = self._make_provider(
            url.hostname.split('.')[0], path)
        return Jams(path, provider, self._config)

    def _parse_url(self, url):
        ''' parsing of the input url
        if url not contains github and gitlab
        then raise exception thats provider is not defined
        '''
        if not url:
            raise InputError("url is not defined")
        return urllib.urlparse(url)

    def _make_provider(self, provider_name, url):
        """
        initialization of provider
        reading of access Github token from environment variable
        """
        if 'GITHUB_TOKEN' not in os.environ:
            raise InputError('GITHUB_TOKEN is not provided')
        return self._providers_inn[provider_name](os.environ['GITHUB_TOKEN'], url)


def parse_yaml(path):
    import yaml
    try:
        with open(path, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
    except IOError as e:
        if e.errno in (errno.ENOENT, errno.EISDIR):
            return
        e.strerror = "Unable to load configuration file {0}".Format(e.strerror)
    return data_loaded


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", help="path to the repo")
    parser.add_argument("--config", help="path to the config")
    parser.add_argument("--not-include", help="not include of checks")
    args = parser.parse_args()
    repo = args.repo
    config = args.config
    if repo is None and config is None:
        raise InputError('Repo or config is not provided')
    a = App('check', '0.1')
    if repo:
        a.build(repo).report()
    if config:
        config_parsed = parse_yaml(config)
        url = config_parsed['url']
        a.add_checkers_from_config(config_parsed)
        a.build(url).report()


if __name__ == '__main__':
    parse_args()
