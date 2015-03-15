SublimeLinter-contrib-JoLint
================================

This linter plugin for SublimeLinter provides an interface to jolint. It will be used with files that have the “__jolie__” syntax.

## Installation

SublimeLinter 3 must be [installed](http://www.sublimelinter.com/en/latest/installation.html) in Sublime Text. I strongly recommend [Package Control](https://packagecontrol.io/installation) for the task.

### Plugin installation

Before using this plugin, you must ensure that `jolint` is installed on your system. To install `jolint` follow the installation steps [here](https://github.com/thesave/jolint) to install the jolint executable

### Plugin installation

You can install the SublimeLinter plugin by copying/cloning it in your SublimeText packages folder.
You can access the packages directory from the main menu *Preferences* -> *Browse Packages*.
Once in the Packages folder you can clone/checkout the repository with 

    svn co https://github.com/thesave/jolint/trunk/SublimeLinter-jolint

After that the plugin shall be installed correctly.

Just open a Jolie source file and start linting :)
