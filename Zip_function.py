if __name__ == '__main__':

    #The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

    a = ("John", "Charles", "Mike")
    b = ("Jenny", "Christy", "Monica", "Vicky")

    x = list(zip(a, b))
    print(x)
    #Output : [('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica')]
    
