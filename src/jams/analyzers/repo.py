from checker import Checker
from output import output
from task import Task
import requests
from urlextract import URLExtract
from spellchecker import SpellChecker

class AnalyzeRepo(Checker):
    def __init__(self, content, url=None, provider=None):
        self._content = str(content)
        self._provider = provider
        super().__init__(str(content), url=url)
    
    def name(self):
        return 'repo'

    def start_message(self):
        """return message before start of repo checks
        """
        print('>Checking of the Repo\n')

    def check(self, repo, **kwargs):
        """check provides checking of Repo
        """
        config = kwargs.get('config')
        checkers = self._make_checkers(names=self._get_checkers_names_from_cfg(config))
        self.score.add_total_checks(len(checkers))
        return sum(checkers)
    
    def _default_checkers(self):
        return []
    
    def _check_issues(self):
        """ provides checking if open issues is exist
        at the directory
        """
        msg = 'Checking of go.mod'
        result = 0 if not self._check_modules() else 1
        output(msg, result)
        self.score.add_check(msg, result)
        return result