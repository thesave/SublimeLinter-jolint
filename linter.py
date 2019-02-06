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

import SublimeLinter
from SublimeLinter.lint import Linter, util
import sublime
import os, platform
import json

class JoLint(Linter):

    """Provides an interface to jolint."""
    syntax = "jolie"
    executable = "jolie"
    if( platform.system() == "Windows" ):
        executable += ".bat"
    # cmd = "jolie --check @"
    regex = (
        r'^.+:(?P<line>\d+): error: (?P<message>.+)$'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = None
    error_stream = util.STREAM_STDERR
    if getattr(SublimeLinter.lint, 'VERSION', 3) > 3:
        from SublimeLinter.lint import const
        ERROR = const.ERROR
    else:
        from SublimeLinter.lint import highlight
        ERROR = highlight.ERROR
    default_type = ERROR
    defaults = {
        "mark_style": "outline",
        "lint_mode": "load_save"
    }

    def cmd(self):
        """Return the command line to execute."""
        if os.environ.get( "JOLIE_HOME" ) is None:
            JOLIE_HOME = Utilities.getJolieHome()
            if JOLIE_HOME is None:
                sublime.message_dialog("Could not find or set JOLIE_HOME properly")
            else: 
                self.env = { "JOLIE_HOME" : JOLIE_HOME }
                
        command = [self.executable, '--check', '$file']
        return command + ['*', '-']

class Utilities():
    def getJolieHome():
        USER_SETTINGS = "SublimeLinter-jolint.sublime-settings"
        WIN_DEF_JOLIE_HOME = "C:\\Jolie"
        NIX_DEF_JOLIE_HOME = "/usr/lib/jolie"
        if( platform.system == "Windows" ):
            DEF_JOLIE_HOME = WIN_DEF_JOLIE_HOME
        else:
            DEF_JOLIE_HOME = NIX_DEF_JOLIE_HOME

        path = os.path.join( sublime.packages_path(), "SublimeLinter-jolint" )
        settings_file = os.path.join( path, USER_SETTINGS )
        if os.path.exists( path ):
            if os.path.isfile( settings_file ):
                try:
                    with open( settings_file, 'r') as settings_content:
                        settings = json.loads( "".join( settings_content.readlines() ) )
                        settings_content.close()
                        return settings[ "JOLIE_HOME" ]
                except Exception as e:
                    sublime.message_dialog("SublimeLinter-jolint could not read the settings file")
            else:
                try:
                    with open( settings_file, 'w', ) as settings_content:
                        settings_content.writelines( json.dumps( { "JOLIE_HOME" : DEF_JOLIE_HOME } ) )
                        settings_content.flush()
                        settings_content.close()
                        sublime.message_dialog( "JOLIE_HOME not set and no settings file found.\n\n"
                                                "JOLIE_HOME set to the default value:\n\n" + DEF_JOLIE_HOME + "\n\n" + 
                                                "Settings file created at:\n\n" + settings_file + "\n\n"
                                                "change the path according to your Jolie installation" 
                                                )
                        return Utilities.getJolieHome()
                except Exception as e:
                    sublime.message_dialog("SublimeLinter-jolint could not write the settings file")
        else:
            sublime.message_dialog( "Could not find the installation directory of SublimeLinter-jolint" )
            return None
