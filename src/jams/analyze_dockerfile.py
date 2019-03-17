from checker import Checker
from output import output

class AnalyzeDockerfile(Checker):
    """ provides analization of the Dockerfile
    https://gist.github.com/Faheetah/a2a401a01d2d56fa7d1a9d7ab0d2831b
    """
    def __init__(self, content, url=None, provider=None):
        self._content = str(content)
        super().__init__(str(content), url=url)
    
    def start_message(self):
        """return message before start of docker checks
        """
        print('Checking of the Dockerfile file\n')
    
    def check(self, url):
        """ checks provides running of all sub-checks
        """
        checks = [self._check_latest(), self._check_run_command()]
        self.score.add_total_checks(len(checks))
        return sum(checks)
    
    def _check_latest(self):
        '''check if Docker file contains pulling from :latest tag
        '''
        docker_file = self._get_dockerfile()
        if not docker_file:
            return 1
        if len(docker_file.find(':latest')) > 0:
            return 0
        output('Checking of the :latest tag', result)
    
    def _check_run_command(self):
        if self._content.find('RUN wget'):
            return 0
        return 1