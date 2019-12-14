from task import Task
from score import Score

class Checker:
    """
    This class defines base class for analyze content
    Every method for check should be named as
    _check_something
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
        check is a main method for making anallize
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
    
    def _default_checkers(self):
        return []
    
    def _make_checkers(self, **kwargs):
        '''
        creating list of checkers for session
        '''
        names = kwargs.get('names')
        if names is None:
            return self._default_checkers()
        checkers = list(filter(lambda x: x[7:] in names, self._get_checkers()))
        return list(map(lambda x: getattr(self, x)(), checkers))
    
    def _get_checkers_names_from_cfg(self, config, name):
        if config is None:
            return
        if 'checkers' not in config:
            return None
        if name not in config['checkers']:
            return None
        return config['checkers'][name]

