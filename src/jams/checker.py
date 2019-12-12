from task import Task
from score import Score

class Checker:
    """
    This class defines base class for analyze content
    """

    def __init__(self, content, task_name='default', url=None):
        self._content = content
        self._task = Task(task_name)
        self._url = url
        self.score = Score()

    def __str__(self):
        return self._content

    def check(self, repo):
        '''
        check is a main method for making analyzation
        of content
        '''
        raise NotImplementedError

    def start_message(self):
        ''' return message which be shown
        before start of checkers
        '''
        raise NotImplementedError
    
    def get_checkers(self):
        '''
        return list of names of checkers
        '''
        raise NotImplementedError
    
    def _get_checkers(self):
        '''
        retrun only methods with starts with _check
        '''
        return list(filter(lambda x: x.startswith('_check'), dir(self)))
