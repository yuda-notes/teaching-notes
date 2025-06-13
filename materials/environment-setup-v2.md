# Environment Setup

## Table of Contents
- [Terminal/CMD](#terminalcmd)
- [VSCode](#vscode)
- [Git](#git)
- [GitHub](#github-classroom)
- [Videos to Watch](#videos-to-watch)

## Terminal/CMD
> Terminal == Command Prompt, just different OS 😁
### Some Popular Commands
- For changing directory
  - **Windows**
    ```
    cd [directory_name]
    ```
    or
    
    ```
    cd [C:\path\to\directory_name]
    ```

    > to go back to previous directory
    > ```
    > cd ..
    > ```
  - **MacOS**
    ```
    cd [directory_name]
    ```
    or
    
    ```
    cd [/path/to/directory_name]
    ```

    > to go back to previous directory
    > ```
    > cd ..
    > ```
- For creating directory (Windows and MacOS)
  ```
  mkdir [directory_name]
  ```
- For displaying directory contents
  - **Windows**
    ```
    dir
    ```
  - **MacOS**
    ```
    ls
    ```
- Other commands
   - [Reference for Windows](https://www.ninjaone.com/blog/windows-cmd-commands/)
   - [Reference for Mac](https://www.techrepublic.com/article/16-terminal-commands-every-user-should-know/)

### Keyboard Shortcuts
- For Windows, learn more about some useful shortcuts [here](https://www.howtogeek.com/254401/34-useful-keyboard-shortcuts-for-the-windows-command-prompt/)
- For Mac, learn more [here](https://www.idownloadblog.com/2020/03/10/mac-keyboard-shortcuts-terminal/)

## VSCode
### Select Default Profile (**Windows only**) ([reference](https://www.shanebart.com/set-default-vscode-terminal/))
1. Open VSCode
2. Press `CTRL + SHIFT + P` on your keyboard to open the **Command Palette**.
3. Search for `Terminal: Select Default Profile`

   <img width="1423" alt="image" src="https://github.com/user-attachments/assets/f94c4b98-5f78-4dd8-9f61-e3643ef50051" /><br/>
4. Select **Command Prompt**

   <img width="1423" alt="image" src="https://github.com/user-attachments/assets/570e01e8-76c3-40ad-b5ce-12e458aa210c" /><br />
5. Close and re-open VSCode.

### Python Files
- There are 2 file extensions that can be used to run python
   - Script file (`.py`)
     - To run a script file, execute the following command in the Terminal
       ```shell
       python filename.py
       ```
       > **Notes**
       > - Make sure to have Conda installed and `base` environment **activated**.
       > - Make sure that the file exist within the **current** directory.
   - Notebook file (`.ipynb`)
     - Notebook is a special extension that can be used to create a report, analysis, or summary using python.
     - Notebook consist of 2 cells component, **markdown/text** and **code**.
     - Markdown/Text cell is used to add narration, explanation, or insight. It is also can be used to give heading for separating each section of the content.
     - Code cell is used to execute a python script within the file.
     - To run a code inside the notebook, we can use the **Run All** button or **Execute** button in each code cell.
    
### `readme.md` File
- **readme.md** file contains the description of current project.
- This file is written using a **Markdown** syntax. You check out these references to understand how that works.
   - [Basic Writing and Formatting - GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
   - [CommonMark](https://commonmark.org/help/)

## Git
### Initial Config ([reference](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
1. Open Terminal/CMD
2. Execute the following command line by line:
   ```shell
   git config --global user.name "John Doe"
   git config --global user.email "johndoe@example.com"
   ```

## GitHub Classroom
### Accepting Assignment From GitHub Classroom ([reference](https://sdsu-research-ci.github.io/github/students/accepting-assignment))
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

### Learn More About Git
- Beginner's Guide to Git [here](https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/)
- Basic Git Command [here](https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/)
- Introduction to Git Branch [here](https://www.geeksforgeeks.org/introduction-to-git-branch/)
- Learn more about Git Workflow [here](https://dev.to/ajmal_hasan/beginner-friendly-git-workflow-for-developers-2g3g)

## Videos to Watch
- [What is Git](https://youtu.be/2ReR1YJrNOM?feature=shared)
- [How Git Works](https://youtu.be/e9lnsKot_SQ?feature=shared)
