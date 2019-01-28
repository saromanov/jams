
class Checker:
    """
    This class defines base class for analyze content
    """

    def __init__(self, content):
        self._content = content

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
