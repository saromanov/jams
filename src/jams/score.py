# -*- coding: utf-8 -*-
"""
    jams.score
    ~~~~~~~~~~~~~
    Implementing score method for calculation of score from checkers 
"""

class Score:
    def __init__(self):
        self._score = 0
    
    def add_total_checks(self, num):
        ''' setting total number of checks
        '''
        self._total = num