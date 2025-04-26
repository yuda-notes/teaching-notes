# OOP

## Definition
- OOP (Object-Oriented Programming) is a programming paradigm that translate code into objects.
- An object can be defined as data that has `attributes` and `behaviour/methods`.
- OOP is just a concept/paradigm in programming, so we can choose to implement or not based on our needs.

## How to Create an Object
- Before creating an Object in OOP, we must first defined a Class.
- Class is a "blueprint" for creating an Object, it defines the attributes and behaviour that the object will have.
- To create a Class, we must use the `class` keyword in Python.
  ```py
  # creating a class
  class Student:
    '''
    Inside of this class we can define the attributes and behaviour/methods.
    '''

    # to define attributes, we must create __init__() method
    def __init__(self, name, address):
      '''
      __init__() method is a "constructor" function that contain statements that are executed when creating an Object.
      Usually, this method can be used to define the attributes for our Object.
      '''

      # defining attributes while assigning values
      self.student_name = name    
      self.student_address = address

    '''
    
    '''
  ```
