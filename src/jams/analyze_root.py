from checker import Checker
from output import output

class AnalyzeRoot(Checker):
    """provides checker for analyze root structure 
    of the project. It can be check licence, contributing, make file, etc
    """
    def __init__(self):
        super().__init__()