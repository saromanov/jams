from analyze import Analyze

class AnalyzeReadme(Analyze):
    def __init__(self, content):
        self._content = str(content)
        self.score = 1
        self._ci = ['https://travis-ci.org', 'https://drone.io/']
        super().__init__(str(content))
    
    def check(self, repo):
        '''
        check_ci provides checking of README.md
        containce badge with ci provider
        '''
        if len(list(filter(lambda x: self._content.find('{0}/{1}'.format(x, repo)) != -1, self._ci))) > 0:
            return 0
        return 1