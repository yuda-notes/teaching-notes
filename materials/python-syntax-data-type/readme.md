# Python Syntax & Data Type

## What We'll Cover

- Basic Syntax
- Python Data Types

## Basic Syntax

- Comments/Docsting

  - Comments are textual notes that will help you and others understand what the code does.
  - To give comments in Python, you must add `#` symbol as prefix.

    ```py
    # This is a comment
    # This is another line of comment
    ```

  - Comments are single-line by default, if you want to have a multi-line comments you must use Docstring.

  - To create Docstring, you must write your text/notes in-between this `'''` symbol

    ```py
    '''
    This is example of a Docstring.
    Docstring is a multi-line comments.
    '''
    ```

## Python Data Types

- String

  ```py
  "This is a String"

  # or
  'This is ALSO a String'

  # or
  'Sebuah kutipan dari Cak Lontong "Berhentilah menuntut Ilmu, karena Ilmu tidak bersalah. Janganlah membalas Budi, karena belum tentu Budi yang melakukan."'
  ```

- Integer

  ```py
  1234

  # or
  1_234
  ```

- Float

  ```py
  1.2

  # or
  1. # output: 1.0
  .1 # output: 0.1

  # or
  1e2 # output: 100.0
  1e-2 # output: 0.01
  ```

- Boolean

  ```py
  True

  # or
  False
  ```

- List

  ```py
  [123, "ABC", 1.2, False, ["x", "y"]]
  ```

- Tuple

  ```py
  (123, "ABC", 1.2, False, ["x", "y"])
  ```

- Dictionary

  ```py
  {
    "name": "Hulk Hogan",
    "birthdate": "1953-08-11"
  }
  ```

- (_EXTRAS_) Set

  ```py
  {1, 2, 1, 1, 3, 2, 4, 3}
  ```
