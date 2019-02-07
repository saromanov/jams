from checker import Checker
from output import output
from score import Score

class AnalyzeDockerfile(Checker):
    """ provides analization of the Dockerfile
    """
    def __init__(self, content):
        self._content = str(content)
        self.score = Score()
        super().__init__(str(content))