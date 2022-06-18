if __name__ == '__main__':

    #print names of planets whose length is less than 6
    planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
    li = [p for subs in planets for p in subs if len(p) < 6]
    print(li)


    #print the matrix
    # [[0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4],
    #  [0, 1, 2, 3, 4]]

    matrix = []
    for i in range(5):
        li = []
        for j in range(5):
            li.append(j)
        matrix.append(li)

    #print(matrix)
    #the same matrix can be achieved using list comprehension
    mat = [[j for j in i]for i in matrix]

    print(mat)

    #flatten the above matrix
    print([j for i in matrix for j in i])
    
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x if x != "banana" else "orange" for x in fruits]
    print(newlist)
