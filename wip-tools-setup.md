# Tools Setup

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
   ![image](https://github.com/user-attachments/assets/23971940-10a2-4483-9216-f62310f1c753)
3. Choose a repository visibility (Public/Private)
4. Select "Initialize this repository with a README".
5. Click "Create repository".

### Clone Repository
1. After creating new repository or if you have existing repository, you can clone your repository to create a local copy on your computer and sync between the two locations.
2. First, navigate to the main page of the repository.
3. Above the list of files, click "Code" button. <br>
   ![image](https://github.com/user-attachments/assets/301165c1-2fcd-4e30-af2d-91f2365f0980)
4. Select "HTTPS" and copy the URL for the repository. <br>
   ![image](https://github.com/user-attachments/assets/0cf23414-86ae-4429-8ffb-0ff5cdb8f8e3)
5. Open Terminal/CMD and execute the following command to clone a repository
   ```shell
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

### GitHub Classroom

-- WIP --
