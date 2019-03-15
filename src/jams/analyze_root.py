from checker import Checker
from output import output


class AnalyzeRoot(Checker):
    """provides checker for analyze root structure
    of the project. It can be check licence, contributing, make file, etc
    """

    def __init__(self, provider):
        super().__init__(provider)
        self._provider = provider

    def check(self, repo):
        return sum([self._check_licence(), self._check_dockerfile()])

    def start_message(self):
        """return message before start of checkers
        """
        return 'Checking of the root structure'
    
    def _check_licence(self):
        """ returns 1 if repo contance licence
        """
        return 0 if not self._get_licence() else 1

    def _get_licence(self):
        '''trying to get licence from repo
        '''
        try:
            return self._provider.get_content_file(
                self._url, 'LICENCE')
        except Exception:
            return None

    def _check_dockerfile(self):
        '''https://gist.github.com/Faheetah/a2a401a01d2d56fa7d1a9d7ab0d2831b
        '''
        docker_file = self._get_dockerfile()
        if not docker_file:
            return 1
        if docker_file.find(':latest'):
            return 0

    def _get_dockerfile(self):
        '''trying to get Dockerfile
        '''
        try:
            return self._provider.get_content_file(
                self._url, '.Dockerfile')
        except Exception:
            return None
