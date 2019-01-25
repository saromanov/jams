from analyze import Analyze
from output import output

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
        result = 0
        checkers = [self._check_ci(repo), self._check_quality_report(), self._check_title()]
        return sum(checkers)
    
    def _check_ci(self, repo):
        '''
        this method trying to parse README.md and find
        badge which is point to CI provider
        '''
        result = len(list(filter(lambda x: self._content.find('{0}/{1}'.format(x, repo)) != -1, self._ci))) > 0
        output('Checking Badge for CI', result)
        return 0 if result else 1
    
    def _check_quality_report(self):
        '''
        this method returns 1 if README not contains quality checker
        at this moment, its checking for Go
        '''
        result = self._content.find('goreportcard.com') == -1 
        output('Checking Badge for code quality', result)
        return 1 if result else 0
    
    def _check_title(self):
        '''
        this method checks if project contains correct
        project title
        '''
        result = self._content.startswith('# ')
        output('Checking correct title', result)
        return 0 if result else 1