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
            This file will be decoded via base64
        '''
        content_file = self._provider.get_content_file(self._url, 'README.md')
        if content_file is None:
            return ''
        return base64.b64decode(content_file.content)
        
