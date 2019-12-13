from analyze_readme import AnalyzeReadme
from analyze_dockerfile import AnalyzeDockerfile
from analyze_root import AnalyzeRoot
from language import GoLang, PythonLang

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
        self._checkers = self._make_checkers()
        self._lang = self._select_language(self.detect_language())
    
    def _make_checkers(self):
        """ 
        returns registered checkers
        if config is not empty, then adding that to the checkers
        """
        if self._config is None or 'checkers' not in self._config:
            return [AnalyzeReadme, AnalyzeDockerfile, AnalyzeRoot]
        checkers = []
        if 'readme' in self._config:
            checkers.append(AnalyzeReadme)
        if 'dockerfile' in self._config:
            checkers.append(AnalyzeDockerfile)
        if 'root' in self._config:
            checker.append(AnalyzeRoot)
        return checkers

    def report(self):
        """ report provides starting of registered checkers
        """
        self._run()

    def _select_language(self, lang):
        if lang == GO_LANG:
            return GoLang(self._provider)
        elif lang == PYTHON_LANG:
            return PythonLang(self._provider)
        else:
            raise NotSupportedLanguageException('language not supported')

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
        for checker in self._checkers:
            r = checker(content_file, provider=self._provider)
            r.start_message()
            r.check(self._url, config=self._config)
        return content_file

    def _get_readme(self):
        '''trying on several ways for getting README file
        with .md, .rst extensions
        '''
        try:
            for path in ['.md', 'rst']:
                content_file = self._provider.get_content_file(
                    self._url, 'README{0}'.format(path))
                if content_file is None:
                    continue
                return content_file
        except Exception:
            return None
