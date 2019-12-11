from checker import Checker
from output import output
from task import Task
import re


class AnalyzeReadme(Checker):
    def __init__(self, content, url=None, provider=None):
        self._content = str(content)
        self._ci = ['https://travis-ci.org', 'https://drone.io/']
        super().__init__(str(content), url=url)

    def start_message(self):
        """return message before start of readme checks
        """
        print('Checking of the README file\n')

    def check(self, repo):
        """check_ci provides checking of README.md
        containce badge with ci provider
        """
        checkers = [self._check_ci(repo),
                    self._check_quality_report(),
                    self._check_title(),
                    self._check_overview()]
        self.score.add_total_checks(len(checkers))
        return sum(checkers)

    def _check_ci(self, repo):
        '''
        this method trying to parse README.md and find
        badge which is point to CI provider
        '''
        result = len(list(filter(lambda x: self._content.find(
            '{0}/{1}'.format(x, repo)) != -1, self._ci))) > 0
        output('Checking Badge for CI', result)
        self.score.add_check('Checking Badge for CI', result)
        return 0 if result else 1

    def _check_quality_report(self):
        '''
        this method returns 1 if README not contains quality checker
        at this moment, its checking for Go
        '''
        result = self._content.find('goreportcard.com') > 0
        output('Checking Badge for code quality', result)
        self.score.add_check('Checking Badge for code quality', result)
        return 1 if result else 0

    def _check_title(self):
        '''
        this method checks if project contains correct
        project title
        '''
        result = self._content.startswith('# ')
        output('Checking correct title', result)
        self.score.add_check('Checking correct title', result)
        return 0 if result else 1
    
    def _check_links(self):
        '''
        this method checkes links on the README files
        return false if readme contains broken links
        '''
        links = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
        output('checking of brokens links')
        broken_links = filter(lambda x: requests.get(x).status_code > 299, links)
        return 0 if len(broken_links) > 0 else 1
        

    def _check_overview(self):
        result = self._content.find(
            '## Getting Started') > 0 or self._content.find('## Overview') > 0
        output('Not contains Getting Started or Overflow parts', result)
        self.score.add_check(
            'Not contains Getting Started or Overflow parts', result)
        return 0 if result else 1
