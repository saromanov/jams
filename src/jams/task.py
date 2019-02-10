# -*- coding: utf-8 -*-
"""
    james.task
    ~~~~~~~~~~~~~
    Implementation of the task. Task this is action which contains 
    checking. It should contains rule, weight
"""

class TaskBase:
    def __init__(self, name, *args, **kwargs):
        self._name = name
    
    def __str__(self):
        return self._name
    
    def __getattr__(self, name):
        return '{0} call'.format(name)
    
    def weight(self):
        """return weight of the task in the case
        if task was completed
        """
        return 0

class Task(TaskBase):
    def __init__(self, name, *args,**kwargs):
        super().__init__(name)
