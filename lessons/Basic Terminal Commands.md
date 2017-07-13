## Basic Terminal Commands



#### **command** *(mnemonic)* - description

**pwd** *(print working directory)* - prints the path of the current terminal session.  This is where  you are in your computers file system.

**ls** (*looksee)* - lists the files and folders in the current working directory.  Can also provide a path to look in i.e. `ls ~/Downloads`

**cd** *(change directory)* - changes the current working directory to the path provided.

**mv** *(move)* - moves a file or folder to the destination you desire.

**which** - tells you the file path of the file associated with a command.  i.e. `which python` to verify you are in a virtual environment.



#### Python Specific

`python3 -m venv env` Creates a new virtual environment (names **env** in this example) in the current directory

`source env/bin/activate` - activates the virtual environment named `env` of the current working directory.

`deactivate` - deactivates the virtual environment and returns the default `python`.

`python` or `ipython` - launches a python REPL

`python some_file.py` - tells the python interpreter to run the code in `some_file.py`

`python —version` - tells you the version of python

`pip install` - installs a python package, i.e. `pip install ipython`

`pip freeze` - lists installed python packages.

**Python packages can be installed in separate environments.**  Ensure you have the correct virtual environment activated before installing a python package.



#### Paths

A file path is a series of folders separated by `/` with an optional file at the end.

The first `/` is also known as the **root** folder.  Paths that start with a `/` are called **absolute paths**.

ex:

`/usr/local/bin/python` 



`.` denotes the current working directory.  So `cd .` has no effect, as it says 'change the current working directory to the current working directory '.

`..` denotes the current working directory's **parent** directory.  So typing `cd ..` when the current working directory is `/Users/somebody/` would take you to `/Users/`

A file path that begins with `.` or `..` is known as a **relative path**.