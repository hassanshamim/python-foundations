# To Create a New Project

1. Create the project folder
   - `mkdir example_folder`
   - `cd example_folder`
2. Create your virtual environment
   - `python3 -m venv example_env` or `python -m env example_env` whichever points to your python3 installation
3. Open your folder in VsCode
   - `File > Open` select `example_folder`
4. Create a new Project in VsCode
   - `cmd+shift+p` (mac) or `ctrl+shift+p`(windows)
   - "Project Manager: Save Project"
   - `enter`
   - Choose a name for the project.  The folder name will be the default.
5. Tell VsCode to use your virtual environment for that project
   - `cmd+shift+p` or `ctrl+shift+p`
   - "Select Workspace interpreter"
   - `enter`
   - A list of python paths will appear.  To direct it to the virtual env inside your project folder type:
   - `./` 
   - You should see a list of paths starting with `./example_env/bin` or whatever you named your virtual environment
   - select either `python` or `python3` - they are the same.



### To activate your virtual environment

1. Open your shell in cmd.exe, git-bash, Terminal.app, or whatever you decide to use
2. Navigate to your project directory
3. type the command
   - Mac/Linux: `source example_env/bin/activate`
   - Windows: `example_env\Scripts\activate`
4. You should now see `(example_env)` in prefixed in your prompt.