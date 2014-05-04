# Consolidated manage module + some top-level commands

from flask.ext.script import Command, prompt, prompt_pass

from .core import sessionStore

from .users.manage import *
# TODO: import custom manage commands


class CleanupSessionsCommand(Command):
    """ Cleanup Sessions in the current app """

    def run(self):
        sessionStore.cleanup_sessions()