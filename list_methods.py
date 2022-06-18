if __name__ == '__main__':

    #append
    fruits = ['apple', 'banana', 'cherry']
    cars = ["BMW","Ferrari"]
    fruits.append('pineapple')
    print(fruits)

    cars.append(fruits)
    print(cars)
    #output : ['BMW', 'Ferrari', ['apple', 'banana', 'cherry', 'pineapple']]

    #count
    numbers = [1,3,5,7,2,4,6,8,2,3,1,9,2,1,9,0]
    print(numbers.count(1))

    #index - returns the first occurance
    print(fruits.index('banana'))

    fruits.extend(['banana','orange','cherry'])
    #index - to return the last occurance
    print(len(fruits) - (fruits[::-1].index('banana')))
    print(fruits)

    #insert
    fruits.insert(3,'guava')
    print(fruits)

    #pop
    fruits.pop(2)
    print(fruits)

    #remove - removes only the first occurance
    fruits.remove('banana')
    print(fruits)

    # Remove all duplicates using a set
    new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon',
                'Black Olive Special', 'Sausage', 'Sausage']
    final_new_menu = list(set(new_menu))
    print(final_new_menu)

    #reverse
    fruits.reverse()

    print(fruits)
