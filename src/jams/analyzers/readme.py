from checker import Checker
from output import output
from task import Task
import requests
from urlextract import URLExtract
from spellchecker import SpellChecker

class AnalyzeReadme(Checker):
    def __init__(self, content, url=None, provider=None):
        self._content = str(content)
        self._ci = ['https://travis-ci.org', 'https://drone.io/']
        super().__init__(str(content), url=url)
    
    def name(self):
        return 'readme'

    def start_message(self):
        """return message before start of readme checks
        """
        print('>Checking of the README file\n')

    def check(self, repo, **kwargs):
        """check_ci provides checking of README.md
        """
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return [
                    self._check_quality_report(),
                    self._check_title(),
                    self._check_overview(),
                    self._check_links(),
                    self._check_misspelling()]

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
        output('Checking correct title', result, details='README file should starts with #')
        self.score.add_check('Checking correct title', result)
        return 0 if result else 1
    
    def _check_links(self):
        '''
        this method checkes links on the README files
        return false if readme contains broken links
        '''
        extractor = URLExtract()
        links = extractor.find_urls(self._content)
        links = list(filter(lambda x: x.startswith('http') and '(' not in x and '\\n' not in x, links))
        broken_links = list(filter(lambda x: requests.get(x).status_code > 299, links))
        output('Checking of brokens links', len(broken_links) == 0)
        self.score.add_check('Repo contains broken links', broken_links)
        return 0 if len(broken_links) > 0 else 1
    
    def _check_misspelling(self):
        '''
        Check of misspelling on the README files
        first, split words from the readme fiels and apply filters
        then, apply corrections and then construct output
        '''
        spell = SpellChecker()
        words = list(filter(lambda x: len(x) > 6 and len(x)< 10, spell.split_words(self._content)))
        new_words = [(spell.correction(word), word) for word in spell.unknown(words)]
        details_output = [] if len(new_words) == 0 else '\n'.join(map(lambda x: '{0} -> {1}'.format(x[1],x[0]), new_words))
        output('Checking of misspelling', len(new_words) == 0, details=details_output)
        self.score.add_check('Checking of misspelling words', len(new_words) == 0)
        return 0 if len(new_words) > 0 else 1

    def _check_overview(self):
        result = self._content.find(
            '## Getting Started') > 0 or self._content.find('## Overview') > 0
        output('Not contains Getting Started or Overflow parts', result)
        self.score.add_check(
            'Not contains Getting Started or Overflow parts', result)
        return 0 if result else 1
