# OOP

## Definition

- OOP (Object-Oriented Programming) is a programming paradigm that translate code into objects.
- An object can be defined as data that has `attributes` and `behaviour/methods`.
- OOP is just a concept/paradigm in programming, so we can choose to implement or not based on our needs.

## How to Create an Object

- Before creating an Object in OOP, we must first defined a Class.
- Class is a "blueprint" for creating an Object, it defines the attributes and behaviour that the object will have.
- Same like building a house, we first need a blueprint of the house before building it, so that we know the specification of our house will have when it finished.
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

    # to define behaviour/method, we must define a function inside the class
    def sayHello(self):
      print("Hi, my name is", self.student_name)
  ```

  > Notice that in each attribute and method, there is a `self` keyword, this is used as a reference to the class itself.
  > So `self.student_name` means that the `student_name` attribute belongs to `Student` class.
  > and `sayHello(self)` means that the `sayHello()` method belongs to `Student` class and the first parameter of this method is always ignored.
- Now, to create an Object we just call the Class name like below.

  ```py
  # calling a class / create an object
  Student(
    student_name="Michael", 
    student_address="Los Angeles"
  )
  ```

- If we print the Object, we get an output like this

  ```py
  print(
    Student(
      student_name="Michael", 
      student_address="Los Angeles"
    )
  )
  # output: <__main__.Student object at 0x7fc9a9e36d60>
  ```

  > Printing an Object will show this arbitrary text that's hard to understand. So to make it more meaningful we use built-in `__str__()` function inside the Class to create custom string.

  ```py
  class Student:
    ...

    # Adding __str__() function 
    def __str__(self);
      '''
      This function will represent an Object with a custom String.
      '''
      return "This is a Student class"

  # print the object again
  print(
    Student(
      student_name="Michael", 
      student_address="Los Angeles"
    )
  )

  # output: "This is a Student class"
  ```

## Accessing the Attributes and Methods From `Student` Object

```py
# create an object and save it to a variable
stu = Student(
      student_name="Michael", 
      student_address="Los Angeles"
    )

print(stu.student_name) # output: Michael
print(stu.student_address) # output: Los Angeles

stu.sayHello() # output: Hi, my name is Michael 
```

## OOP Characteristics

- There are many characteristics that are assosciated with OOP.
  - Inheritance
  - Encapsulation
  - Abstraction
  - Polymorphism

### Inheritance

- Inheritance is a concept in OOP that allows Class to inherit its attributes and methods from other Class.
- Just like inheritance in real-life, in OOP there are also a parent Class and child Class, where child will inherit their parents attribute and also their methods.

```py
# parent class
class Foo:
  '''
  Foo class is a parent class, this means that all attributes and methods 
  from this class will be inherited to its child.
  '''
  def __init__(self):
    self.name = "John Doe"
  
  def hello(self):
    print("hello world")

# child class
class Bar(Foo):
  '''
  Bar class is a child of Foo, this means that in this class will have all of
  its parent's attributes and methods.
  '''
  pass

# create Bar object
barObj = Bar()

# access attributes from child
print(barObj.name) # output: John Doe

# access method from child
barObj.hello() # output: hello world
```

### Types of Inheritance

![](https://miro.medium.com/v2/resize:fit:1089/0*utVulhXRC5VWsSq5.jpg)

## Reference

- <https://www.geeksforgeeks.org/python-oops-concepts/>
