#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Saverio Giallorenzo
# Copyright (c) 2015 Saverio Giallorenzo
#
# License: MIT
#

"""This module exports the jolint plugin class."""



from SublimeLinter.lint import Linter, util
import os

class JoLint(Linter):

    """Provides an interface to jolint."""
    syntax = "jolie"
    cmd = "jolie --check @"
    regex = (
        r'^.+:(?P<line>\d+): error: (?P<message>.+)$'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH

    if os.environ.get( "JOLIE_HOME" ) is None:
        env = { "JOLIE_HOME" : "/usr/lib/jolie" }
