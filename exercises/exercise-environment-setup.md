# Environment Setup - Exercise

## Create New Conda Environment

1. Create a new environment with the following format: `env_[your_name]` ([reference](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands))

    ```bash
    conda create --name [env_name] python
    ```

2. Activate your new environment ([reference](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment))
3. Inside your new environment, install `pyjokes` package with `pip` command

    ```bash
    pip install [package_name]
    ```

4. Try the package after install by typing `pyjoke` or `pyjokes` command in the Terminal.
5. Go back to `base` environment, by deactivating current environment
6. Report to the instructor if finished

## Create New GitHub Repository

1. Create an new repository on GitHub and then clone the repo to your local directory

   ```bash
   git clone [your_git_url]
   ```

2. Open your cloned folder with VSCode
3. Create a markdown file `readme.md` with the following content:

    ```md
    # My First Project

    ## Introduction
    - Name: ...
    - Batch: ...
    ```

4. Create a python script file `main.py` with the following code:

    ```py
    print("Hi! this is my first script")
    ```

5. Create a notebook file `notes.ipynb` with the following content:
    - Add one markdown/text cell and insert this text

        ```md
        # My Notebook

        ## Introduction
        - Name: ...
        ```

    - Add one code cell and insert this code

        ```py
        print("This code will be executed.")
        ```

    - Execute all code cell by clicking the "Execute" button in each cell or "Run All" button on top of the file.
6. Make sure to save all files!
7. Open VS Code integrated terminal and perform these commands:
    1. Execute the python script

        ```bash
        python main.py
        ```

    2. Git add

        ```bash
        git add .
        ```

    3. Git commit

        ```bash
        git commit -m "commit_message"
        ```

    4. Git push

        ```bash
        git push
        ```

        but, if this is the first push, then you **must do** this

        ```bash
        git push --set-upstream origin main
        ```

8. Report to the instructor if finished.

## Learn GitHub Classroom

1. Accept the assignment from [this link](https://classroom.github.com/a/hSnP3gZD)
2. Follow the instruction on the screen until your repository is auto-generated.
   <img width="664" alt="image" src="https://github.com/user-attachments/assets/a637c672-88a6-48db-97a0-937b65400f08" />
3. Clone the repository and open it with VS Code.
4. Create a new file called `[your_name].md` with the following content:

    ```md
    # My First Repo from Classroom

    - Name: ...
    - [insert 1 motivational/funny/meme quotes that you can think of]
    ```

5. Make sure to save all files.
6. Perform the following command in your Terminal/CMD:
   - git add
   - git commit
   - git push
7. Report to the instructor if finished
