from analyze_readme import AnalyzeReadme
from analyze_dockerfile import AnalyzeDockerfile
from language import GoLang, PythonLang


class DetectLanguageException(Exception):
    pass


class NotSupportedLanguageException(Exception):
    pass


class Jams:
    ''' Jams class provides implementation of the user logic
        all handling insede the app. Getting files, analyzing, etc
    '''

    def __init__(self, url, provider):
        self._provider = provider
        self._url = url
        self._checkers = [AnalyzeReadme, AnalyzeDockerfile]
        self._lang = self._select_language(self.detect_language())

    def start(self):
        self.check_readme()

    def _select_language(self, lang):
        if lang == 'Go':
            return GoLang(self._provider)
        elif lang == 'Python':
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

    def register_checker(self, name):
        '''register checker provides registration of checker
        '''
        pass

    def check_readme(self):
        ''' return content of the README.md file
        '''
        print(self._provider.get_repo(self._url).language)
        content_file = self._get_readme()
        if content_file is None:
            return ''

        for checker in self._checkers:
            r = checker(content_file)
            r.start_message()
            r.check(self._url)
            print(r)
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
