#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Saverio Giallorenzo
# Copyright (c) 2015 Saverio Giallorenzo
#
# License: MIT
#

"""This module exports the JoLint plugin class."""

from SublimeLinter.lint import Linter, util


class JoLint(Linter):

    """Provides an interface to JoLint."""
    # r'^Failure: \[(?P<line>\d+)\.(?P<col>\d+)\] failure: (?P<message>.+)$'

    syntax = "jolie"
    cmd = "jolint @"
    executable = None
    regex = (
        r'^.+:(?P<line>\d+): error: (?P<message>.+)$'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r''