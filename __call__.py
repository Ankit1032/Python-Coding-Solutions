# callable(python_object) ---- returns ---> boolean value (True if passed object is callable else False)
# callable objects are objects which can be called anytime like functions
# Objects having __call__() method in their class is called callable objects

x = 100

def add(a,b):
    return a+b

class ABC():

    def __init__(self,a,b):
        self.a = a
        self.b = b

print(callable(x)) # Integer objects are not callable
print(callable(add)) #This happens internally---> add.__call__(10,20) means a __call__ method be already defined in functions internally
print(add.__call__(10,20))

print(callable(ABC)) # Even classes are callable as they internally get __call__() created.

ob1 = ABC(1,2)
print(callable(ob1)) # Instances/Objects of classes are not callable

# Now lets make the object/instance of a class callable so we will have to define __call__() method in the class

class Dog():

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __call__(self,c):
        print(f"Number of dogs : {self.a+self.b+c}")

ob2 = Dog(6,10) #Triggers only __init__
print(callable(ob2)) #Now this object/instance is callable
ob2(100) #--> Internally this happens --> ob2.__call__() --> Triggers __call__()