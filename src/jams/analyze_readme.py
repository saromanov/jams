
class AnalyzeReadme:
    def __init__(self, content):
        self._content = content
        self.score = 1
        self._ci = ['https://travis-ci.org', 'https://drone.io/']
    
    def check_ci(self):
        '''
        check_ci provides checking of README.md
        containce badge with ci provider
        '''
        pass