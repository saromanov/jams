# -*- coding: utf-8 -*-
"""
    james.language
    ~~~~~~~~~~~~~
    Implementing language classes which conteins specific
    checks for each language
"""


class Language:
    """Definition of the base class for language
    """

    def __init__(self, provider):
        self._provider = provider
    
    def get_checkers(self):
        ''' return checkers specified for the language
        '''
        raise NotImplemented
    
    def _get_file(self, name, url):
        """trying to get file
        """
        try:
            return self._provider.get_content_file(
                url, name)
        except Exception:
            return None


class GoLang(Language):
    """Provide checking specific for Go lang
    """

    def __init__(self, provider):
        Language.__init__(self, provider)
    
    def get_checkers(self):
        ''' return specified for GoLang
        '''
        return [self._check_modules]
    
    def _check_modules(self):
        return self._get_file('go.mod', None)



class PythonLang(Language):
    """Provide checking specific for python
    """

    def __init__(self, provider):
        Language.__init__(self, provider)
