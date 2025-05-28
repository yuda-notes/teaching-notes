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

## Loops ([reference](https://www.geeksforgeeks.org/loops-in-python/))
- **Loops** in Python are used to execute certain blocks of code repeatedly.
- There are 2 types of loop, indefinite (`while` loop) and definite (`for` loop).
- Just like conditionals, loop can also be nested with each other.

### `while` Loop
- It is used to execute a block of statements repeatedly until a given condition is satisfied.
![image](https://github.com/user-attachments/assets/b74c4c5d-78a2-4c9e-9368-1bcad616a43e)

```py
count = 0
while (count < 3):        # this is the condition
    count = count + 1     # this block statement will be executed if the condition is still True
    print("Hello World!")
```

#### Infinite Loop
- While loop can be used to create an infinite loop which is a loop that never ends. This is because the condition is always be True.
<img src="https://github.com/user-attachments/assets/4f54f8ff-a588-401e-90a3-538c23130adb" width="500"> <br>
```py
count = 0
while (count < 3):        # this is the condition
    print("Hello World!") # this block statement will be executed infinitely because "count" value will stay 0, so the condition will always be True
```

### `for` Loop
- It is used for traversing a collection data type, like **List**, **Tuple**, **Range**, **Dictionary**, **Set** and also **String**.
- Traversal is the process of visiting or processing each node.
![image](https://github.com/user-attachments/assets/01f11d21-565e-4917-90e4-4d6e97598e74)
```py
for x in [1,2,3,4,5]:
    print(x)
```

### `else` statement
- A loop can also have an `else` statement. It is used to execute code after the loop finishes.
```py
# `while` example
count = 0
while (count < 3):               # this is the condition
    count = count + 1            # this block will be executed if the condition is still True
    print("Hello World!")
else:
    print("Finished, see you!")  # this block will be executed if the condition is False/loop has finished

# `for` example
for count in [0,1,2]:
    print(count)
else:
    print("Finished, see you!")  # this block will be executed if the loop has finished
```

### `break` and `continue`
- **break** is a keyword to terminate a loop entirely
- **continue** is a keyword to skip the current iteration of a loop and move to the next iteration. It is useful when we want to bypass certain conditions without terminating the loop.

## Comprehensions ([reference](https://www.geeksforgeeks.org/comprehensions-in-python/))
- **Comprehensions** in Python provide a concise and efficient way to create new sequences from existing ones.
- There are 4 types of comprehensions:
    -  List (`list`)
    -  Dictionary (`dictionary`)
    -  Set (`set`)
    -  Generator (`range()`)
-  In comprehensions we can add conditional `if` to filter specific item from the existing collection
```py
# Example of list comprehensions without condition
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a]
print(res) # output [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example of list comprehensions with condition
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = [num for num in a if num % 2 == 0]
print(res) # output [2, 4, 6, 8]
```
