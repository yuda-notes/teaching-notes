# Conditionals and Loops

## Conditionals ([reference](https://www.geeksforgeeks.org/conditional-statements-in-python/))
- Conditional statements are used to execute certain blocks of code based on **specific conditions**.
- These statements help **control the flow** of a program, making it behave differently in different situations.
- Conditionals can also be nested.
![image](https://github.com/user-attachments/assets/8dbbe35a-4752-4269-8102-4740671383e2)

### `if` Statement
- It is the simplest form of conditional.
- It executes a block of code if the given condition is true.
```py
age = 20

if age >= 18:                  # this is the condition/expression
    print("Eligible to vote.") # this statement will be executed if the condition is True
```

> Note: The executed statement can be written in multiple lines.

### `if-else` Statement
- The addition of `else` block provides a way to handle all other cases that don't meet the specified conditions.
```py
age = 20

if age >= 18:
    print("Eligible to vote.")                     # this statement will be executed if the condition is True
else:
    print("Sorry, you are not eligible to vote.")  # this statement will be executed if the condition is False
```
#### Ternary Operator
- **Ternary Operator** is essentially a shorthand for the `if-else` statement.
- It allows us to write more compact code especially for **simple condition**.
```py
age = 20
print("Eligible to vote.") if age >= 18 else print("Sorry, you are not eligible to vote.")
```

> Note: In Ternary Operator, both `if` and `else` can only have 1 line of statement to be executed.

### `if-elif-else` Statement
- `elif` allows us to check **multiple conditions**, providing a way to execute **different blocks of code** based on which condition is true
```py
score = 80

if score >= 80:
    print("Grade: A")     # this statement will be executed if the first condition is True
elif score >= 70:
    print("Grade: B")     # this statement will be executed if the second condition is True
else:
    print("Grade C")      # this statement will be executed if both first and second condition are False
```

## Loops
