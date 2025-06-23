# Teaching Notes

- For H8
  - Tools installation, please refer to this [link](https://gist.github.com/yudantoanas/f50b15eb71290964b9abfbf2573a7bab)
  - Conda environment please follow this tutorial
    1. Download `h8_env.yml` file from [here](https://drive.google.com/file/d/1XP9QUaqexuDEb8sd3VdpzqMkAx0FmsRH/view?usp=drive_link) or [here](https://gist.github.com/yudantoanas/e439226b0064097b07178afa9772078e)
    2. Execute the following command on Terminal/Command Prompt
        ```shell
        conda env create -f /path/to/h8_env.yml
        ```
          - Example, files in `C:\Documents\h8_env.yml` (Windows) or `/Users/yudanto/h8_env.yml` (MacOS)
            ```shell
            conda env create -f C:\Documents\h8_env.yml
      
            # OR
            conda env create -f /Users/yudanto/h8_env.yml
            ```
    3. After create environment, you can do this command
       ```shell
       conda activate h8_env
       ```
         - To check env list, you can use this command
           ```shell
           conda env list
           ```
