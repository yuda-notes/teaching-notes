# Loop

## Menu App
- Create an app that can receive an input from the user (hint: you can use `input()` function)
- This app will do some process based on the selected menu.
    - menu `1`: create a fibonacci sequence
      > use this code to complete the process for menu `1`
      ```py
        n = 10
        num1 = 0
        num2 = 1
        next_number = num2  
        count = 1
        result = [num1, num2]
        
        while count <= n:
            count += 1
            num1, num2 = num2, next_number
            result.append(next_number)
        
            next_number = num1 + num2
        
        print(result)
      ```
    - menu `2`: determine even/odd date
      > use this code to complete the process for menu `2`
      ```py
        currentDate = 1 # you can change the value to today's date
        
        if currentDate % 2 == 0:
            print("it's even date")
        else:
            print("it's odd date")
      ```
    - menu `3` or `exit`: the app will stop
- If user choose a menu, either `1`, `2, `3`, or `exit`, the app will process it based on the selection.
- Otherwise, the app will display an error that says "menu is not valid, try again!".
- This app will keep running until the user choose `3` or `exit.
