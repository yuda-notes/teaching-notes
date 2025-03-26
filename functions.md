# Functions

## Definition ([reference](https://www.geeksforgeeks.org/python-functions/))
- Function is a set of instruction that does specific job
- Benefits of Using Functions
  - **Readability** 
  - **Reusability**

![image](https://github.com/user-attachments/assets/bed4b959-5474-4788-8594-3dd2d0d100d2)

## Create Function
![image](https://github.com/user-attachments/assets/539ff73f-49d8-4481-ba67-50ec055597d5)

```py
# create a function
def fun():
    print("Hello World")
```

- After creating a function in Python we can call it by using the name of the functions.
  ```py
  # calling a function
  fun() # output "Hello World"
  ```

## Parameters/Arguments
- Parameters/Arguments are the values passed inside the parenthesis of the function.
- A function can have any number of arguments separated by a comma.

### Types of Arguments
- Default argument
  - Default argument is a parameter that assumes a default value.
    ```py
    def fun(arg1=10):
      pass

    fun(5) # if given a value, this value will replace the default value
    ```
- Keyword arguments (named arguments)
  - The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
    ```py
    def fun(arg1):
      pass

    fun(arg1=5) # this will give context that `5` will be stored in `arg1` no matter the position.
    ```
- Positional arguments
  - We used the Position argument during the function call so that the first value for first argument, second value for second argument, and so on.
    ```py
    def fun(arg1, arg2):
      pass

    fun(10, 4) # `10` will be stored in `arg1` and 4 will be in `arg2`
    ```
- Variable-Length arguments (`*args` and `**kwargs`)
  - By default, each argument can only store single value. In Variable-Length arguments, we can define a single argument that can store multiple values by using special symbol (`*` and `**`)
    ```py
    def fun(*arg1):
      pass

    fun(1, 2, 3, 4, 5) # these values will be collected as tuple

    def fun(**arg1):
      pass

    fun(A=1, B=2, C=3, D=4, E=5) # these values will be collected as dictionary
    ```
 
## Anonymous Function
- **Anonymous function** is a function without a name.
- Using `lambda` keyword to create anonymous function.
  ```py
  # since anonymous function doesn't have a name, in order to be called, a lambda must be stored inside a variable.
  result = lambda x1, x2: x1/x2

  # calling lambda function
  result(10,2) # output: 5
  ```

## Module/Package
- **Module** is the equivalent of script file.
- **Package** is the equivalent of folder, it consists of many modules.
```py
# import module
import module_name

# import module inside a package
import package_name.module_name

# import module using `from`
from module_name import var_name, func_name

# import module inside a package using `from`
from package_name.module_name import var_name, func_name
```
