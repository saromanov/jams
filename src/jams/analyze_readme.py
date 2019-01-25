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
        result = self._check_ci(repo) + self._check_quality_report(repo)
        return result
    
    def _check_ci(self, repo):
        '''
        this method trying to parse README.md and find
        badge which is point to CI provider
        ''' 
        if len(list(filter(lambda x: self._content.find('{0}/{1}'.format(x, repo)) != -1, self._ci))) > 0:
            return 0
        return 1
    
    def _check_quality_report(self, repo):
        '''
        this method returns 1 if README not contains quality checker
        at this moment, its checking for Go
        '''
        return 1 if self._content.find('goreportcard.com') == -1 else 0