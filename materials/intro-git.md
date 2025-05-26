# Git 101

- **Git** is a Version Control System (VCS) that helps **track code changes** and **collaborate** with others.
  <img src="https://cdn.idntimes.com/content-images/community/2021/08/screenshot-20210816-170647-6ff4389e5b5ccef71e70121535467561-0c3e9947ed9df8a18cdf77be3f9c9175_600x400.jpg" width="500">

## Setup
1. Download and install Git from [here](https://git-scm.com/downloads).
2. Verify git version
    ```shell
    git -v
    ```
3. After installing git, you can do these initial config just once.
    ```shell
    # set git username -> same as github username
    git config --global user.name "John Doe"
    
    # set git email -> same as github email
    git config --global user.email "johndoe@example.com"
    ```

## Create a git project
1. Create new project directory and open it in VSCode
2. Open new terminal in VSCode.
3. Make sure to run this in your project directory.
    ```shell
    git init
    ```
4. Now you can do whatever you like in this project, whether adding new files, modifying files/folders, etc.

### Committing changes
1. If you have made any changes in your project, you can save all files (`ctrl` + `s`) and track all changes with this command
    ```shell
    git add .

    # or, to track changes from specific file
    git add file.txt

    # or, track changes from specific folder in current directory
    git add /folder1
    ```
    - to check if you have perform `git add` or not you can use this command
        ```shell
        git status
        ```
2. Now you can commit your changes with this command
    ```shell
    # be careful of mistyping this command
    git commit -m "commit message"
    ```
3. After your changes has been committed, you can make another changes too (just start again from step `1`).

## GitHub
- **GitHub** is a cloud-based platform where you can store, share, and work together with others to write code. ([reference](https://docs.github.com/en/get-started/start-your-journey/about-github-and-git#about-github))
- Each source code is stored within a repository.

### Create Personal Repository ([reference](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository))
1. Open GitHub and click "Create New Repository" button.
2. Type a name for your repository, and an optional description. <br>
   <img src="https://github.com/user-attachments/assets/23971940-10a2-4483-9216-f62310f1c753" alt="drawing" width="500">
4. Choose a repository visibility (Public/Private)
5. Select "Initialize this repository with a README".
6. Click "Create repository".

### Clone Repository ([reference](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))
1. If you have an existing repository, you can clone your repository to create a local copy on your computer and sync between the two locations.
2. First, navigate to the main page of the repository.
3. Above the list of files, click "Code" button. <br>
   <img src="https://github.com/user-attachments/assets/301165c1-2fcd-4e30-af2d-91f2365f0980" alt="drawing" width="500">
4. Select "HTTPS" and copy the URL for the repository. <br>
   <img src="https://github.com/user-attachments/assets/0cf23414-86ae-4429-8ffb-0ff5cdb8f8e3" alt="drawing" width="500">
5. Open Terminal/CMD and execute the following command to clone a repository
   ```shell
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   ```

### Pushing commit to GitHub
- If you have made changes to your project and you have perform `git commit`, you can push your changes to GitHub with this command
    ```shell
    git push
    ```
- To make sure your push is successfull, you can refresh your repository page to see the latest update(s).

### Learn More About Git
- Beginner's Guide to Git [here](https://github.blog/developer-skills/programming-languages-and-frameworks/what-is-git-our-beginners-guide-to-version-control/)
- Basic Git Command [here](https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/)
- Introduction to Git Branch [here](https://www.geeksforgeeks.org/introduction-to-git-branch/)
- Learn more about Git Workflow [here](https://dev.to/ajmal_hasan/beginner-friendly-git-workflow-for-developers-2g3g)