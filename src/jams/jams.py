import base64

class Jams:
    ''' Jams class provides implementation of the user logic
        all handling insede the app. Getting files, analyzing, etc
    '''
    def __init__(self, url, provider):
        self._provider = provider
        self._url = url
    
    def start(self):
        self.get_readme()
    
    def get_readme(self):
        ''' return content of the README.md file
        '''
        content_file = self._get_readme()
        print(content_file)
        if content_file is None:
            return ''
        return content_file
    
    def _get_readme(self):
        '''trying on several ways for getting README file
        with .md, .rst extensions
        '''
        try:
            for path in ['.md', 'rst']:
                content_file = self._provider.get_content_file(self._url, 'README{0}'.format(path))
                if content_file is None:
                    continue
                return content_file
        except:
            return None
        
