from checker import Checker
from output import output
from score import Score

class AnalyzeDockerfile(Checker):
    """ provides analization of the Dockerfile
    https://gist.github.com/Faheetah/a2a401a01d2d56fa7d1a9d7ab0d2831b
    """
    def __init__(self, content):
        self._content = str(content)
        self.score = Score()
        super().__init__(str(content))
    
    def _check_latest(self):
        '''check if Docker file contains pulling from :latest tag
        '''
        docker_file = self._get_dockerfile()
        if not docker_file:
            return 1
        if len(docker_file.find(':latest')) > 0:
            return 0
        output('Checking of the :latest tag', result)