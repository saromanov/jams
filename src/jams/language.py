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