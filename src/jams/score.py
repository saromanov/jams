# -*- coding: utf-8 -*-
"""
    jams.score
    ~~~~~~~~~~~~~
    Implementing score method for calculation of score from checkers
"""


class Score:
    def __init__(self):
        self._score = 0
        self._checks = {}

    def add_total_checks(self, num):
        ''' setting total number of checks
        '''
        self._total = num

    def add_check(self, name, score):
        ''' setting check to the known checks
        '''
        self._checks[name] = score

    def result(self):
        '''retruns result from all checks
        '''
        for k, v in self._checks.items():
            print(k, v)
