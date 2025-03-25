# Basic Python

## Syntax ([reference](https://www.geeksforgeeks.org/python-comments/))
- Everything that we write inside our code editor can be execute, except for "Comments"
- **Comments** in Python are the lines in the code that are ignored by the interpreter during the execution of the program.
- Comments enhance the readability of the code, it can be used to identify and explain functionality of the code.

## Data Type ([reference](https://www.w3schools.com/python/python_datatypes.asp))
- `string`: for Word, Sentence, or Character(s)
  ```py
  "this is a string"
  'this is also a string'
  "I am a 'string' inside of string"
  ```
- `integer`: for whole number
  ```py
  1 2 3 4 5
  ```
- `float`: for decimal number
  ```py
  1.0
  2.
  3.5
  0.3
  .4e2  # same as 0.4 * 10^2
  .5e-3 # same as 0.5 * 10^-3
  ```
- `boolean`: True or False
  ```py
  True
  False
  ```
- `list`: collection of values/data (mutable)
  - Lists are ordered by its index.
  - Lists can contain any arbitrary objects/data types.
  - Lists can be nested.
  - Lists are dynamic
  ```py
  [1,2,3]
  ["a","b","c"]
  ```
- `tuple`: collection of values/data (immutable)
  - Have some similarity with `list`, except for `immutable`.
  ```py
  (1,2,3)
  ("a","b","c")
  ```
- `dictionary`: collection of mapped-values
  - It is mutable, just like a `list`
  - It is dynamic.
  - It can be nested
  - It doesn't have an index, but it has **keys** where each key has it's own value.
  ```py
  {
    "A": 123,
    "B": "XYZ"
    "C": [1,3,5]
  }
  ```

### String Manipulation
- A string can be manipulated using `+` and `*` symbol
- Example of `+` manipulation:
  ```py
  # this process is also called "concatenation" or "concat" for short
  "hello" + "world"

  # concat can only be used with another string, not with other data types
  "hello" + "world" # this is valid
  "hello" + 123 # this is invalid
  ```
- Example of `*` manipulation:
  ```py
  # `*` will repeat a string N times
  "hello" * 3 # output: "hellohellohello"

  # this symbol can only be used with integer
  "ang" * 3 # this is valid
  "hello" * "world" # this is invalid
  ```

## Variable
- **Variable** is a temporary storage for any data
- Variable name can be in any length
- A variable name can have an uppercase or lowercase or both and can use `_` symbol if it's multi-word name.
- The first character cannot be digit
- There are many types of variable naming:
  - camelCase
  - PascalCase
  - snake_case

### Operator
- **Operator** is a symbol in python.
- Operator are divided into following groups
  - Assignment `=`
  - Arithmetic `+ - * / % ** //`
  - Comparison `== != < <= > >=`
  - Logical `and or`
- If operator combined with a value or a variable it is called an **expression**
 
### List manipulation
```py
# create an empty list
list = []

# populate the empty list
list.append("data") # the list will have ["data"]

# access an item inside a list
list[10] # `10` is the index number

# change the value for specific index
list[10] = 100

# slicing a list
list[1:5] # slice from index 1 up to 4 (5-1)
```

### Tuple Manipulation
```py
# create a Tuple
tup = (1,2,3,4,5)

# change the value for specific index
tup[10] = 100 # invalid syntax

# slicing a tuple
tup[:5] # slice from index 0 up to 4 (5-1)
```

### Dictionary Manipulation
```py
# create a dictionary
di = {
  "k1": 123,
  "k2": "abc"
}

# access a value from dict
di["k1"]

# add new key-value pair
di["k3"] = True

# edit existing key-value pair
di["k2"] = [1,2,3]
```
