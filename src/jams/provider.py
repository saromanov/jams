
class Provider:
    def __init__(self, token):
        self._token = token
    
    def token(self):
        return self._token