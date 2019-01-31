from checker import Checker
from output import output

class AnalyzeRoot(Checker):
    """provides checker for analyze root structure 
    of the project. It can be check licence, contributing, make file, etc
    """
    def __init__(self, provider):
        super().__init__()
        self._provider = provider
    
    def start_message(self):
        """return message before start of checkers
        """
        return 'Checking of the root structure'

    def _get_licence(self):
        '''trying to get licence from repo
        '''
        try:
             return self._provider.get_content_file(
                    self._url, 'LICENCE')
        except Exception:
            return None
    
    def _get_dockerfile(self):
        '''trying to get Dockerfile
        '''
        try:
            return self._provider.get_content_file(
                    self._url, 'LICENCE')
        except Exception:
            return None
