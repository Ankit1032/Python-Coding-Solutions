
if __name__ == '__main__':

    num = int(input("Enter a number: "))
    array = [9,6,0,4,2,3,5,1,8,7]

    mat=[]

    for index in range(1,len(array)):
        for j in range(index):
            if array[index] + array[j] == num:
                mat.append([array[index] ,array[j]])

    print(mat)
