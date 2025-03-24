# Exercise VSCode

1. Launch VS Code and then open folder that you have previously built on "Exercise Bash" session
2. Add 2 files inside the folder:
   - 1 **script** file: `[your_name]_script.py`
   - 1 **notebook** file: `[your_name]_notebook.ipynb`
3. Copy/paste the script below to your **script** file and save.
   ```py
   print("Hello, [your_name]!")
   ```
4. In **notebook** file, create 1 `code` cell and 1 `markdown/text` cell with following requirements:
   - In `code` cell: copy/paste the script below
     ```py
     print("Hello, [your_name] from notebook!")
     ```
   - In `markdown/text` cell: write down your name and batch like below
     ```
     - name: [your_name]
     - batch: [your_batch]
     ```
     **Notes**:
     - Batch format: `[branch_code]-[batch_number]`
        - Example: `HCK-012`
     - For **Pondok Indah** campus the code is `HCK`
     - For **Remote** campus the code is `RMT`
   - Execute the code by clicking "Run All" button on top of the file or "Execute" button on each code cell. 
   - Save the file
5. Open Terminal/Anaconda Prompt
   - Make sure to have your current directory is the same as the folder you've opened in VSCode.
      - In Windows (CMD), just look for the current directory section behind your cursor in the CMD.
        ![image](https://storage.googleapis.com/static.configserverfirewall.com/images/windows10/cmd/print-working-directory-windows.webp)
      - In MacOS or Linux: use `pwd` command to see your current directory.
   - If current directory is **NOT* the same as the folder you've opened in VSCode, use `cd` command to change directory to a designated folder.
   - Make sure there are files exists by using `dir` (Windows) or `ls` (MacOS/Linux) command.
6. Execute the `script` file using `python` command in your Terminal.
   ```bash
   python [your_name]_script.py
   ```
7. Report to the instructor if finished
     
