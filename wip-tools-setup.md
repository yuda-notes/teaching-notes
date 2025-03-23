# Tools Setup

## Table of Contents
- [Conda](#conda)
- [Git](#git)
- [VSCode](#vscode)
- [Terminal/CMD](#terminalcmd)
- [GitHub](#github)

## Conda
### Check Version/`conda` Command
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

Reference:
- https://saturncloud.io/blog/solving-the-conda-command-not-recognized-issue-on-windows-10/

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

## Terminal/CMD
### Shell Commands
- For Windows, learn more about some useful commands [here](https://www.ninjaone.com/blog/windows-cmd-commands/)
- For Mac/Linux, learn more [here](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/) or [here](https://www.digitalocean.com/community/tutorials/linux-commands#top-50-linux-commands-you-must-know-as-a-regular-user)

### Keyboard Shortcuts
- For Windows, learn more about some useful shortcuts [here](https://www.howtogeek.com/254401/34-useful-keyboard-shortcuts-for-the-windows-command-prompt/)
- For Mac/Linux, learn more [here](https://www.idownloadblog.com/2020/03/10/mac-keyboard-shortcuts-terminal/) or [here](https://itsfoss.com/linux-terminal-shortcuts/)

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
