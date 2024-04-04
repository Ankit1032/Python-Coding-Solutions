# The __init__ method, on the other hand, is an instance method that is responsible for initializing the newly created object.
class Person:
    def __init__(self, name, age):
        print("Initializing the Person object")
        self.name = name
        self.age = age

person = Person("John Doe", 30)
print(f"Person's name: {person.name}, age: {person.age}")