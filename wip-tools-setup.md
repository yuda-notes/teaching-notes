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

## Conda
### Check version
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
   - Just to make sure, open Anaconda Prompt and write `where conda` it will give you the same pattern like above.

-- WIP --
