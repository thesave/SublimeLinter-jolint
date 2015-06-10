SublimeLinter-jolint
================================

This linter plugin for SublimeLinter provides an interface to jolint. It will be used with files that have the “__jolie__” syntax.

## Installation

SublimeLinter 3 must be [installed](http://www.sublimelinter.com/en/latest/installation.html) in Sublime Text. I strongly recommend [Package Control](https://packagecontrol.io/installation) for the task.

### Installation

Before using this plugin, you must ensure that `jolie` is installed on your system. To install `jolie` follow the installation steps [here](http://www.jolie-lang.org/download.html).

### Plugin installation

#### Automatic Installation via Package Control

Using Package Control is strongly recommended.

Make sure you installed Package Control and proceed with the following:

- bring up the Command Palette (Default <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> or <kbd>⌘</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>);
- type install;
- among the commands you should see Package Control: Install Package. Select the command;
- Package Control will fetch the list of available plugins;
- type "jolie", among the entries you should see "SublimeLinter-jolint". Select it;
- Package Control will install the package.

#### Manual installation via git

You can install the SublimeLinter plugin by copying/cloning it in your SublimeText packages folder.
You can access the packages directory from the main menu *Preferences* -> *Browse Packages*.
Once in the Packages folder you can clone/checkout the repository with 

    git clone https://github.com/thesave/SublimeLinter-jolint

After that the plugin shall be installed correctly.

Just open a Jolie source file and start linting :)

## To Do

- [ ] add dependency to [SublimeLinter3](https://github.com/SublimeLinter/SublimeLinter3);
- [x] after installation, add a pop-up to set environmental variable "JOLIE_HOME" for Mac/Linux (right now hard-coded in linter.py).
