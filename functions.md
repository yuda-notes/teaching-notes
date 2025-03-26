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
- Keyword arguments (named arguments)
  - The idea is to allow the caller to specify the argument name with values so that the caller does not need to remember the order of parameters.
- Positional arguments
  - We used the Position argument during the function call so that the first value for first argument, second value for second argument, and so on. 
- Variable-Length arguments (`*args` and `**kwargs`)
  - By default, each argument can only store single value. In Variable-Length arguments, we can define a single argument that can store multiple values by using special symbol (`*` and `**`)
 
## Anonymous Function
- **Anonymous function** is a function without a name.
- Using `lambda` keyword to create anonymous function.
- 
