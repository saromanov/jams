from analyze_readme import AnalyzeReadme


class Jams:
    ''' Jams class provides implementation of the user logic
        all handling insede the app. Getting files, analyzing, etc
    '''

    def __init__(self, url, provider):
        self._provider = provider
        self._url = url
        self._checkers = [AnalyzeReadme]

    def start(self):
        self.check_readme()

    def register_checker(self, name):
        '''register checker provides registration of checker
        '''

    def check_readme(self):
        ''' return content of the README.md file
        '''
        content_file = self._get_readme()
        if content_file is None:
            return ''

        for checker in self._checkers:
            r = checker(content_file).check(self._url)
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
