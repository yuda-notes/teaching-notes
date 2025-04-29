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

# calling a function
fun() # output "Hello World"
```

## Parameters/Arguments

- Parameters/Arguments are the values passed inside the parenthesis `()` of the function.
- A function can have any number of arguments separated by a comma.

### Types of Arguments

- Positional arguments
  - By default, we must pass values into a function by considering their argument position

    ```py
    def fun(arg1, arg2):
      pass

    # based on argument position, `arg1` = 10, `arg2` = 4
    fun(10, 4)
    ```

- Default argument
  - Argument can also have a default value

    ```py
    def fun(arg1=10):
      pass

    # if given a value, this will replace the default value
    fun(5)
    ```

- Keyword arguments (named arguments)
  - We can pass value(s) to a function without considering their position, just by calling the argument name.

    ```py
    def fun(arg1, arg2):
      pass

    '''
    `arg1` will have 5 and `arg2` will have 10
    '''
    fun(arg2=10, arg1=5) 
    ```

- Variable-Length argument (`*args` and `**kwargs`)
  - By default, each argument can only store single value.
  - In Variable-Length, an argument can store multiple values by using special symbol (`*` and `**`).

    ```py
    # *args argument
    def fun(*arg1):
      pass

    # these values will be collected as tuple
    fun(1, 2, 3, 4, 5) 

    # **kwargs argument
    def fun(**arg1):
      pass

    # these values will be collected as dictionary
    fun(A=1, B=2, C=3, D=4, E=5)
    ```

## Anonymous Function

- We can define a function without a name, hence the name is **Anonymous**.
- Using `lambda` keyword to create anonymous function.

  ```py
  # a lambda function must be stored inside a variable.
  result = lambda x1, x2: x1/x2

  # calling lambda function
  result(10,2) # output: 5
  ```

## Module/Package

- **Module** is the equivalent of script file `.py`.
- **Package** is the equivalent of folder/directory.

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
