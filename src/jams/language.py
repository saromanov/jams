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


class GoLang(Language):
    """Provide checking specific for Go lang
    """

    def __init__(self, provider):
        Language.__init__(self, provider)


class PythonLang(Language):
    """Provide checking specific for python
    """

    def __init__(self, provider):
        Language.__init__(self, provider)
