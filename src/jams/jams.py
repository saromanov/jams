from analyzers.readme import AnalyzeReadme
from analyzers.docker import AnalyzeDockerfile
from analyzers.root import AnalyzeRoot
from analyzers.language import GoLang, PythonLang
from analyzers.repo import AnalyzeRepo

GO_LANG = 'Go'
PYTHON_LANG = 'Python'


class Jams:
    ''' Jams class provides implementation of the user logic
        all handling insede the app. Getting files, analyzing, etc
    '''

    def __init__(self, url, provider, config, *args, **kwargs):
        self._provider = provider
        self._url = url
        self._config = config
        self._specified_checkers = self._select_language(
            self.detect_language)
        self._checkers = self._make_checkers()

    def _make_checkers(self):
        """
        returns registered checkers
        if config is not empty, then adding that to the checkers
        """
        if self._config is None or 'checkers' not in self._config:
            return [
                self._specified_checkers,
                AnalyzeReadme,
                AnalyzeDockerfile,
                AnalyzeRoot]
        checkers = []
        checker = self._config['checkers']
        if 'readme' in checker:
            checkers.append(AnalyzeReadme)
        if 'dockerfile' in checker:
            checkers.append(AnalyzeDockerfile)
        if 'root' in checker:
            checkers.append(AnalyzeRoot)
        if 'golang' in checker:
            checkers.append(GoLang)
        if 'repo' in checker:
            checkers.append(AnalyzeRepo)
        return checkers

    def report(self):
        """ report provides starting of registered checkers
        """
        self._run()

    def _select_language(self, lang):
        ''' getting specified checkers for the language
        '''
        result = lang()
        if result == GO_LANG:
            return GoLang
        elif result == PYTHON_LANG:
            return PythonLang
        else:
            raise NotSupportedLanguageException('language is not supported')

    def detect_language(self):
        '''provides detecting of the language by request to the
        repo and getting language from this
        '''
        language = self._provider.get_repo(self._url).language
        if not language:
            raise DetectLanguageException('unable to detect language')
        return language

    def register_checker(self, check):
        """register checker provides registration of checker
        """
        self._checkers.append(check)

    def _run(self):
        ''' return content of the README.md file
        '''
        content_file = self._get_readme()
        if content_file is None:
            return ''
        score = 0
        for checker in self._checkers:
            r = checker(content_file, provider=self._provider)
            r.start_message()
            r.check(self._url, config=self._config)
            score += r.get_score()
        print('Score: {0} of {1} {2:.2%}'.format(
            score, len(self._checkers), score / len(self._checkers)))
        return content_file

    def _get_readme(self):
        '''trying on several ways for getting README file
        with .md, .rst extensions
        '''
        try:
            for path in ['.md', '.rst', 'txt']:
                content_file = self._provider.get_content_file(
                    self._url, 'README{0}'.format(path))
                if content_file is None:
                    continue
                return content_file
        except NotSupportedLanguageException:
            return None
