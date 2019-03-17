from checker import Checker
from output import output


class AnalyzeRoot(Checker):
    """provides checker for analyze root structure
    of the project. It can be check licence, contributing, make file, etc
    """

    def __init__(self, content, url=None, provider=None):
        super().__init__(provider, url=url)
        self._provider = provider
        self._content = content
        self._provider = provider

    def check(self, repo):
        return sum([self._check_licence(), self._check_dockerfile()])

    def start_message(self):
        """return message before start of checkers
        """
        print('Checking of the root structure\n')
    
    def _check_licence(self):
        """ returns 1 if repo contance licence
        """
        msg = 'Checking of the Licence'
        result = 0 if not self._get_licence() else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result
    
    def _check_gomod(self):
        """ provides checking if go.mod is exist
        at the directory
        """
        msg = 'Checking of go.mod'
        result = 0 if not self._get_licence() else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result

    def _check_dockerfile(self):
        '''provides checking of the Dockerfile
        '''
        msg = 'Checking of the Dockerfile at the root'
        result = 0 if not self._get_dockerfile() else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result

    def _get_dockerfile(self):
        '''trying to get Dockerfile
        '''
        return self._get_file('Dockerfile')
    
    def _get_licence(self):
        '''trying to get licence from repo
        '''
        return self._get_file('LICENSE')
    
    def _get_file(self, name):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                self._url, name)
        except Exception:
            return None
