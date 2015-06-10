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
import os, platform
import codecs
import json

class JoLint(Linter):

    def checkEnvironment():
        USER_SETTINGS = "SublimeLinter-jolint.sublime-settings"
        windows_default = "C:\jolie"
        nix_default = "/usr/lib/jolie"
        if( platform.system == "Windows" ):
            default_install = windows_default
        else:
            default_install = nix_default

        if os.environ.get( "JOLIE_HOME" ) is None:
            path = os.path.join( sublime.packages_path(), "SublimeLinter-jolint" )
            settings_file = os.path.join( path, USER_SETTINGS )
            if os.path.exists( path ):
                if os.path.isfile( settings_file ):
                    with codecs.open( settings_file, 'r', 'UTF-8') as settings_content:
                        settings = json.loads( "".join( settings_content.readlines() ) )
                        if settings[ "JOLIE_HOME" ]:
                            os.environ[ "JOLIE_HOME" ] = settings[ "JOLIE_HOME" ]
                else:
                    with codecs.open( settings_file, 'w', 'UTF-8' ) as settings_content:
                        settings_content.writelines( json.dumps( { "JOLIE_HOME" : default_install } ) )
                        sublime.message_dialog( "JOLIE_HOME not set and no settings file found.\n\n"
                                                "JOLIE_HOME set to the default value:\n\n" + default_install + "\n\n" + 
                                                "Settings file created at:\n\n" + settings_file + "\n\n"
                                                "change the path according to your Jolie installation" 
                                            )
                        checkEnvironment()
        else :
            print("\"JOLIE_HOME\" is set to " + os.environ.get( "JOLIE_HOME" ) )

    sublime.message_dialog("Plugin activated")

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

    checkEnvironment()
    env = { "JOLIE_HOME" : os.environ[ "JOLIE_HOME" ] }

