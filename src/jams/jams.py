
class Jams:
    ''' Jams class provides implementation of the user logic
        all handling insede the app. Getting files, analyzing, etc
    '''
    def __init__(self, provider):
        self._provider = provider
    
    def start(self):
        self._provider.get_readme()
    
    def get_readme(self):
        ''' return content of the README.md file
            after this, this file will be analyzed
            if README file is not found, then its return 
            error and downgrade score
        '''
        content_file = self._provider.get_content_file('README.md')
        print(content_file)
        if content_file is None:
            return 
        
