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
import sublime
import os
import codecs

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
    USER_SETTINGS = "SublimeLinter-jolint.sublime-settings"

    if True: #os.environ.get( "JOLIE_HOME" ) is None:
        path = os.path.join( sublime.packages_path(), "SublimeLinter-jolint" )
        settings_file = os.path.join( path, USER_SETTINGS )
        if os.path.exists( path ):
            if os.path.isfile( settings_file ):
                sublime.message_dialog("USER_SETTINGS path: " + settings_file )
                with codecs.open( settings_file, 'r', 'UTF-8') as settings:
                    settings.readlines()
            else:
                sublime.message_dialog("USER_SETTINGS file does not exist, creating" )
                with codecs.open( settings_file, 'w', 'UTF-8' ) as settings:
                    settings_file.writelines( { "JOLIE_HOME" : "/usr/lib/jolie" } )

        # Set JOLIE_HOME according to your installation path
        env = { "JOLIE_HOME" : "/usr/lib/jolie" }
    else :
        sublime.message_dialog("\"JOLIE_HOME\" is set to " )

