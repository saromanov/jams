# -*- coding: utf-8 -*-
from checker import Checker
from output import output

"""
    james.analyzers.language
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
    
    def name(self):
        return 'golang'
    
    def start_message(self):
        """return message before start of checkers
        """
        print('\n>Checking of Golang repo\n')
    
    def check(self, repo, **kwargs):
        """check_ci provides checking of README.md
        """
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return [
                    self._check_gomod(),
                    self._check_godoc_link()
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
    
    def _check_godoc_link(self):
        """ provides checking of link to gomod
        on README.md
        """
        msg = 'Checking of godoc link'
        result = 0
        readme = self._get_file('README.md', None)
        if 'godoc' in readme.split():
            result = 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result

    
    def _check_modules(self):
        '''
        provides checking of go.mod file is exist
        at teh root of the dir
        '''
        return 0 if not self._get_file('go.mod', None) else 1
    
    def _get_file(self, name, url):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                url, name)
        except IOError:
            return None



class PythonLang(Checker):
    """Provide checking specific for python
    """

    def __init__(self, provider):
        Checker.__init__(self, provider)
    
    def name(self):
        return 'python'
    
    def start_message(self):
        """return message before start of checkers
        """
        print('\n>Checking of Python repo\n')
    
    def check(self, repo, **kwargs):
        """check provides checking of the repo
        """
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return [
                    self._check_setup()
                ]
    
    def _check_setup(self):
        """ provides checking if setup.py is exist
        at the directory
        """
        msg = 'Checking of setup.py'
        result = 0 if not self._get_file('setup.py', None) else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result
    
    def _check_versions(self):
        ''' provides checking of actual versions based on setup.py
            Its not make sense to check versions on 2.x, since
            support of this is depricated
        '''
        setup = self._get_file('setup.py', None)
        if not setup:
            return 0
        supported = ['3.5','3.6','3.7', '3.8']
        beginning = 'Programming Language :: Python :: '
        for line in setup.split('\n'):
            if not line.startswith(beginning):
                continue
            data = line.split(beginning)[1]
            if len(data) < 2:
                continue
            data = data[0:len(data)-2]
            if data in supported:
                supported.remove(data)
        msg = 'checking of supported versions'
        result = 0 if len(supported) > 0 else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result

    def _check_toxini(self):
        """ provides checking if tox.ini is exist
        at the directory
        """
        msg = 'Checking of tox.ini'
        result = 0 if not self._get_file('tox.ini', None) else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result
    
    def _get_file(self, name, url):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                url, name)
        except Exception:
            return None
