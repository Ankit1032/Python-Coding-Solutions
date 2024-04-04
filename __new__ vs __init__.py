# The new method is a static method that belongs to the class itself. It’s responsible for creating and returning a new instance of the class.
# The __new__ method is called before the __init__ method and is often used when you need to control the object creation process, like in the case of singletons or when you want to inherit from immutable classes.

"""
Differences Between __new__ and __init__
1. __new__ is a static method, while __init__ is an instance method.
2. __new__ is responsible for creating and returning a new instance, while __init__ is responsible for initializing the attributes of the newly created object.
__new__ is called before __init__.
__new__ can return any object, while __init__ must return None.
"""

"""
For example, you might want to use __new__ to:

Ensure that the object is of a certain type.
Set the object’s initial state.
Prevent the object from being created.
"""

"""
You should use __init__ when you need to initialize the object. For example, you might want to use __init__ to:

Set the object’s attributes.
Call the object’s superclass’ __init__ method.
Perform other initialization tasks.
"""

class Person:
    def __new__(cls, name, age):
        print("Creating a new Person object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age):
        print("Initializing the Person object")
        self.name = name
        self.age = age

person = Person("John Doe", 30)
print(f"Person's name: {person.name}, age: {person.age}")