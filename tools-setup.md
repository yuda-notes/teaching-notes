# Tools Setup

## Table of Contents
- [Anaconda](#anaconda)
- [VSCode](#vscode)
- [Terminal/CMD](#terminalcmd)
- [Git](#git)
- [GitHub](#github)

## Anaconda
### Definition
- Anaconda is an open-source distribution of Python and R programming languages, mainly suitable for Data Science projects.
- Miniconda is a smaller version of Anaconda, both have same functionality and features.
- **Conda** is a CLI app that enables user to manage packages and environments.
- **Environment** is an isolated workspace that contains a specific collection of packages. ([reference](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html#what-is-a-conda-environment))
  ![image](https://github.com/user-attachments/assets/17222b6b-68d2-4a8a-a940-cbbcc11bf8ad)

### Conda Cheatsheet ([reference](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf))
    ```bash
     # verify conda installation or check version
     conda --version
   
     # check current environment
     conda info
   
     # Display list of environments. The active environment will be labeled with asterisk (*) symbol
     conda info --envs
   
     # install package named "Pandas"
     conda install pandas
   
     # install package with specific version
     conda install selenium=1.2
   
     # remove/uninstall package
     conda remove scipy
   
     # Display list of installed packages in current environment
     conda list
   
     # create new environment named "Env1"
     conda create --name Env1
   
     # create new environment with python and pandas package installed
     conda create --name Env1 python pandas
   
     # delete specific environment
     conda remove --name Env1 --all
   
     # activate specific environment
     conda activate Env1
   
     # deactivate environment (base)
     conda deactivate
   
     # update conda to the latest version (if available)
     conda update conda
    ```

### Pip Cheatsheet ([reference](https://opensource.com/sites/default/files/gated-content/cheat_sheet_pip.pdf))

- Just like `conda`, `pip` command is also can be used to manage packages within the environment.
- To use `pip` command it is required to have python installed in the environment.

```bash
# install package with latest version
pip install pandas

# install package with specific version
pip install pandas==2.0.0

# remove/uninstall package
pip uninstall scipy

# Display list of installed packages in current environment
pip list
```

### Troubleshoot `conda command not recognized` (**Windows only**) ([reference](https://saturncloud.io/blog/solving-the-conda-command-not-recognized-issue-on-windows-10/))
1. Open Terminal/CMD
2. Execute `conda --version`, it will display the version number.
3. In Windows, if it displays "conda command not recognized", open the Start Menu and search for "Environment Variables".
4. Click on "Edit the system environment variables".
5. In the System Properties window, click on "Environment Variables". <br>
   ![image](https://github.com/user-attachments/assets/93a65a8b-c5a4-4b1d-ba50-0a460462ac8d)
6. In the Environment Variables window, under "System variables", find and select "Path", then click on "Edit". <br>
   ![image](https://github.com/user-attachments/assets/f0d1d61a-58ef-4d99-be3a-1d7f5b3ed04d)
7. In the Edit Environment Variable window, click on "New". <br>
   ![image](https://github.com/user-attachments/assets/142cdbda-b908-4bd8-9659-b33afb77c8e2)
8. Add the path to the directory where Conda is installed. This is typically in `C:\Users\YourUsername\Anaconda3\Scripts`.
   - Just to make sure, open Anaconda Prompt and execute `where conda` command. It will give you the same output pattern like above.
9. Click "OK" on all windows to save the changes.
10. Close and reopen Terminal/CMD.

## VSCode
### Select Default Profile (**Windows only**)
1. Press `CTRL + SHIFT + P` to open the Command Palette
2. Search for `Terminal: Select Default Profile`
   ![image](https://github.com/user-attachments/assets/f94c4b98-5f78-4dd8-9f61-e3643ef50051)
3. Select `Command Prompt` <br>
   ![image](https://github.com/user-attachments/assets/570e01e8-76c3-40ad-b5ce-12e458aa210c)
4. Close and reopen the VSCode.

Reference:
- https://www.shanebart.com/set-default-vscode-terminal/

### Python Quickstart
- There are 2 file extensions that can be used to run python
   - Script file: `.py`
     - To run a script file, execute the following command in the Terminal
       ```shell
       python filename.py
       ```
       > **Notes**
       > - Make sure to have Conda installed and is using `base` environment.
       > - Make sure that the file exist within the current directory.
   - Notebook file: `.ipynb`
     - Notebook is a special extension that can be used to create a report, analysis, or summary using python.
     - Notebook consist of 2 cells component, **markdown/text** and **code**.
     - Markdown/Text cell is used to add narration, explanation, or insight. It is also can be used to give heading for separating each section of the content.
     - Code cell is used to execute a python script within the file.
     - To run a code inside the notebook, we can use the **Run All** button or **Execute** button in each code cell.

## Terminal/CMD
### Shell Commands
- For Windows, learn more about some useful commands [here](https://www.ninjaone.com/blog/windows-cmd-commands/)
- For Mac/Linux, learn more [here](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/) or [here](https://www.digitalocean.com/community/tutorials/linux-commands#top-50-linux-commands-you-must-know-as-a-regular-user)

### Keyboard Shortcuts
- For Windows, learn more about some useful shortcuts [here](https://www.howtogeek.com/254401/34-useful-keyboard-shortcuts-for-the-windows-command-prompt/)
- For Mac/Linux, learn more [here](https://www.idownloadblog.com/2020/03/10/mac-keyboard-shortcuts-terminal/) or [here](https://itsfoss.com/linux-terminal-shortcuts/)

## Git
### Git Config
1. Open Terminal/CMD
2. Execute the following command line by line:
   ```shell
   git config --global user.name "John Doe"
   git config --global user.email "johndoe@example.com"
   ```

Reference:
- https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

## GitHub
### Create Empty Repository
1. Open GitHub and click "Create New Repository" button.
2. Type a name for your repository, and an optional description. <br>
   <img src="https://github.com/user-attachments/assets/23971940-10a2-4483-9216-f62310f1c753" alt="drawing" width="500">
4. Choose a repository visibility (Public/Private)
5. Select "Initialize this repository with a README".
6. Click "Create repository".

Reference: 
- https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

### Clone Repository
1. After creating new repository or if you have existing repository, you can clone your repository to create a local copy on your computer and sync between the two locations.
2. First, navigate to the main page of the repository.
3. Above the list of files, click "Code" button. <br>
   <img src="https://github.com/user-attachments/assets/301165c1-2fcd-4e30-af2d-91f2365f0980" alt="drawing" width="500">
4. Select "HTTPS" and copy the URL for the repository. <br>
   <img src="https://github.com/user-attachments/assets/0cf23414-86ae-4429-8ffb-0ff5cdb8f8e3" alt="drawing" width="500">
5. Open Terminal/CMD and execute the following command to clone a repository
   ```shell
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

Reference:
- https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

### GitHub Classroom
1. Click [here](https://classroom.github.com/a/hSnP3gZD) to accept demo assignment from Classroom.
2. You may be prompted to sign in. <br>
   <img src="https://github.com/user-attachments/assets/3f1dca1b-2c47-422e-8ce1-e58dddee144f" alt="drawing" width="500">
3. If this is your first time using GitHub Classroom, you may be prompted to authorize GitHub Classroom. <br>
   <img src="https://github.com/user-attachments/assets/c2830987-b004-4e36-b8c2-81f18cc35d70" alt="drawing" width="500">
4. If this is your first time accepting an assignment for a classroom, you may be prompted to associate your GitHub account to your registered name. <br>
   <img src="https://github.com/user-attachments/assets/6a1aa07e-4cc6-40ec-b023-d1cbcc1cb159" alt="drawing" width="500"> <br>
   > Carefully select your name, if you click the wrong name please notify your instructor so they can unlink the account.
5. Click the “Accept this assignment” button <br>
   <img src="https://github.com/user-attachments/assets/9e82cb9c-b454-407b-9777-c88d35ddc6d5" alt="drawing" width="500">
6. Click the link to view you repository <br>
   <img src="https://github.com/user-attachments/assets/c35a21a6-1573-413b-9583-21902fadec4d" alt="drawing" width="500">
7. You can clone this repository as usual.

Reference:
- https://sdsu-research-ci.github.io/github/students/accepting-assignment

### What's Next
- Learn more about basic git [here](https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/)
- Learn more about git branch [here](https://www.geeksforgeeks.org/introduction-to-git-branch/)
- Learn more about Git Workflow [here](https://dev.to/ajmal_hasan/beginner-friendly-git-workflow-for-developers-2g3g)
