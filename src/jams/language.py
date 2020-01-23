# -*- coding: utf-8 -*-
from checker import Checker
from output import output

"""
    james.language
    ~~~~~~~~~~~~~
    Implementing language classes which conteins specific
    checks for each language
"""

class GoLang(Checker):
    """Provide checking specific for Go lang
    """

    def __init__(self, content, url=None, provider=None):
        self._provider = provider
        self.content = content
        self._url = url
        Checker.__init__(self, provider)
    
    def start_message(self):
        """return message before start of checkers
        """
        print('\nChecking of Golang repo\n')
    
    def check(self, repo, **kwargs):
        """check_ci provides checking of README.md
        """
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config, 'readme'))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return [
                    self._check_gomod()
                ]
    
    def _check_gomod(self):
        """ provides checking if go.mod is exist
        at the directory
        """
        msg = 'Checking of go.mod'
        result = 0 if not self._check_modules() else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result
    
    def _check_modules(self):
        return self._get_file('go.mod', None)
    
    def _get_file(self, name, url):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                url, name)
        except Exception:
            return None



class PythonLang(Checker):
    """Provide checking specific for python
    """

    def __init__(self, provider):
        Checker.__init__(self, provider)
