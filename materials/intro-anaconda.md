# Anaconda 101

- **Anaconda** is an open-source distribution of Python and R programming languages, mainly suitable for Data Science projects.
- There is a smaller version of Anaconda called **Miniconda** which have same functionality and features but different in size usage.
- **Conda** is a CLI app that enables user to manage packages and environments.
- Conda can be accessed with **Anaconda Prompt** or with built-in **Terminal** (MacOS/Linux) and **CMD** (Windows)
- **Environment** is an isolated workspace that contains a specific collection of packages. ([reference](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/02-working-with-environments/index.html#what-is-a-conda-environment))
  ![image](https://github.com/user-attachments/assets/17222b6b-68d2-4a8a-a940-cbbcc11bf8ad)

## Setup
- Please refer to this tutorial [here](https://gist.github.com/yudantoanas/f50b15eb71290964b9abfbf2573a7bab#anaconda)

## Managing Package Installation
- **Install** package
  ```shell
  # install package named "Pandas"
  conda install pandas

  # or, install package with specific version
  conda install selenium=1.2
  ```
- **Remove** package
  ```shell
  # remove package named "Pandas"
  conda remove pandas
  ```
- **Display** list of installed packages
  ```shell
  conda list
  ```

### PIP
- We can also use `pip` command to manage our package installations.
- `pip` is a package manager in `python` package.

```shell
# install package with latest version
pip install pandas

# install package with specific version
pip install pandas==2.0.0

# remove/uninstall package
pip uninstall scipy

# Display list of installed packages in current environment
pip list
```

## Managing Conda Environment
- **Check** current environment
  ```shell
  # check current environment
  conda info

  # or, to display list of environments. 
  # The active environment will be labeled with an asterisk (*) symbol
  conda info --envs
  ```
- **Create** new environment
  ```shell
  # create new environment named "Env1"
  conda create --name Env1

  # or, create new environment with 'python' and 'pandas' package installed
  conda create --name Env1 python pandas
  ```
- **Remove** existing environment
  ```shell
  conda remove --name Env1 --all
  ```
- **Activate/Deactivate** specific environment
  ```shell
  # activate specific environment
  conda activate Env1

  # deactivate environment
  conda deactivate
  ```
## External References
- [What is Anaconda](https://youtu.be/iaNEQglCF-I?feature=shared)
