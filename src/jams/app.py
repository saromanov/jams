import argparse

class App(object):
    def __init__(self, description, version, command_manager):
        self.command_manager = command_manager