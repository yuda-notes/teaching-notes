# Tools Installation

## Table of Contents
- [Anaconda](#anaconda)
- [VSCode](#vscode)
- [Git](#git)
- [Tableau](#tableau)
- [PostgreSQL](#postgresql)
- [Docker](#docker)

## Anaconda
Follow the instructions based on your Operating Systems: [Windows](#windows) or [MacOS](#macos)
### Windows
1. Download and install from this [link](https://www.anaconda.com/download/success)
   - Choose only **one** between Distribution Installer (Anaconda) or Miniconda Installer.
     <img width="1423" alt="image" src="https://github.com/user-attachments/assets/cb912890-c014-4d72-a9dd-d5459158ec14" />
2. Follow the installation steps until finished.
3. Check and verify conda via Command Prompt.
   - Open Command Prompt and execute this command
     ```shell
     conda --version
     ```
     
   - If you have an error like `conda is not recognized as internal or external command`, then follow these steps:
      1. Open Anaconda Prompt and execute this command
           ```
           where conda
           ```
  
         <img width="1423" alt="image" src="https://github.com/user-attachments/assets/7cb14fcd-be27-46cb-abf1-9c2302da0255" />

      2. Copy the line that says `C:\Users\[your_name]\Anaconda3\Scripts` or something similar based on your system.
      3. Open Advanced System Settings
     
         <img width="1423" alt="image" src="https://i.sstatic.net/W1loq.png" />
         
      4. Click on Environment Variables

         <img width="1423" alt="image" src="https://i.sstatic.net/TUBh9.png" />

      5. Edit `Path`

         <img width="1423" alt="image" src="https://i.sstatic.net/OytYj.png" />

      6. Add your copied path from **step 2** and paste in here.

         <img width="1423" alt="image" src="https://i.sstatic.net/9WbkZ.png" />

      7. Click `OK` to apply settings.
      8. Re-open the Command Prompt and try execute `conda --version` command again.
      9. You should see the conda version and that's it.
> Video tutorial [here](https://youtu.be/yFeVEAeOcnE)
### MacOS
1. Download and install from this [link](https://www.anaconda.com/download/success)
   - Choose only **one** between Distribution Installer (Anaconda) or Miniconda Installer.
     <img width="1423" alt="image" src="https://github.com/user-attachments/assets/cb912890-c014-4d72-a9dd-d5459158ec14" />
2. Follow the installation steps until finished.
3. Check and verify conda via Terminal.
   - Open Terminal and execute this command
     ```shell
     conda --version
     ```
   - You should see the conda version and that's it.
> Video tutorial [here](https://youtu.be/DNu8pQOYRGg)

## VSCode
- Download and install from this [link](https://code.visualstudio.com/download), choose **one** based on your OS.
- Follow the installation steps until finished.

## Git
### Installation
#### Windows
- Download and install the standalone app from this [link](https://git-scm.com/downloads/win)
- Follow the installation steps until finished.
- Check and verify git installation with this command
  ```
  git --version
  ```
#### MacOS
- Download and install the standalone app from this [link](https://git-scm.com/downloads/mac)
- It's recommended to choose `Homebrew` method to install Git.
  1. Install Homebrew from this command
     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
  2. Wait until finished and then execute this command
     ```
     brew install git
     ```
- Check and verify git installation with this command
  ```
  git --version
  ```

### Initial Config ([reference](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup))
1. Open https://github.com/ and register account with your personal email.
2. Open Terminal/Command Prompt and execute the following command
   - Set git username - same as your **GitHub** username
     ```shell
     git config --global user.name "John Doe"
     ```
   - Set git email - same as your **GitHub** email
     ```shell
     git config --global user.email "john.doe@mail.com"
     ```
## Tableau
- Download and install from this [link](https://www.tableau.com/products/public/download)
  - **Note**: You must register an account before downloading
- Follow the installation steps until finished.

## PostgreSQL (+ pgAdmin)
### Windows
- Download and install from this [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- Follow the installation steps until finished.
  **Notes**:
  - During the installation, it's recommended that you don't check the `Stack Builder` option.
  - For username and password you can use this configuration:
    ```
    username: postgres
    password: postgres
    ```
  - For port number just follow the default settings or `5432`
### MacOS
- It's recommended that you have `Homebrew` installed, please refer to [Git](#git) section -> MacOS installation.
- For download and install using `Homebrew` you can use this command
  ```
  brew install postgresql
  ```
- For download and install **without** using `Homebrew` you can use this [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
- Follow the installation steps until finished.

> For both Windows and MacOS users that have install PostgreSQL using this [link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) you don't need to install pgAdmin again because it's already included in the installation package.

> **But**, For MacOS users that have install PostgreSQL using `Homebrew`, you must download and install **pgAdmin** separately from this [link](https://www.pgadmin.org/download/pgadmin-4-macos/)

## Docker
- Download and install from this [link](https://www.docker.com/products/docker-desktop/)
- Follow the installation steps until finished.
> **Notes** for Windows users, you may need to install WSL2 first, please refer to this [link](https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command) for the installation tutorial on how to install WSL2.

> For other reference: https://www.freecodecamp.org/news/how-to-install-wsl2-windows-subsystem-for-linux-2-on-windows-10/
