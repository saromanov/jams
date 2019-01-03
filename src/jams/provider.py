
class Provider:
    def __init__(self, token):
        self._token = token
    
    def token(self):
        return self._token
    
    def get_repository(self, name):
        pass
    
    def get_open_issues(self):
        pass