if __name__ == '__main__':

    #num = int(input("Enter a number: "))
    array = [22,2,12,38,5,8,10,50]

    if array[0] > array[1]:
        max_1st = array[0]
        max_2nd = array[1]
    else:
        max_1st = array[1]
        max_2nd = array[0]

    for i in range(2,len(array)):
        if array[i] >= max_1st:
            max_2nd = max_1st
            max_1st = array[i]


    print("max: ",max_1st, "|| 2nd max: ",max_2nd)
