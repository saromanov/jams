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
    
    def name(self):
        return 'root'

    def check(self, repo, **kwargs):
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return [
                    self._check_license(),
                    self._check_gitignore()
                ]

    def start_message(self):
        """return message before start of checkers
        """
        print('\n>Checking of the root structure\n')
    
    def _check_license(self):
        """ returns 1 if repo contance license
        """
        msg = 'Checking of the license'
        result = 0 if not self._get_license() else 1
        output(msg, result, details='LICENCE file is not found')
        self.score.add_check(msg, result)
        return result

    def _check_dockerfile(self):
        '''provides checking of the Dockerfile
        '''
        msg = 'Checking of the Dockerfile at the root'
        result = 0 if not self._get_dockerfile() else 1
        output(msg, result, details='Dockerfile is not found')
        self.score.add_check(msg, result)
        return result
    
    def _check_gitignore(self):
        '''
        checking if gitignore file is exist on the repo
        '''
        msg = 'Checking of the .gitignore at the root'
        result = 0 if not self._get_gitignore() else 1
        output(msg, result, '.gitignore file is not found')
        self.score.add_check(msg, result)
        return result

    def _get_dockerfile(self):
        '''trying to get Dockerfile
        '''
        return self._get_file('Dockerfile', self._url)
    
    def _get_gitignore(self):
        '''trying to get .gitignore
        '''
        return self._get_file('.gitignore', self._url)
    
    def _get_license(self):
        '''trying to get license from repo
           at this moment quick and dirty check
           of the license contains
        '''
        license = self._get_file('LICENSE', self._url)
        return True if b'License' in license and b'Copyright' in license else False
    
    def _get_file(self, name, url):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                url, name)
        except Exception:
            return None
