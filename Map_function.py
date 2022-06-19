if __name__ == '__main__':

    #Code1
    num_list = [2,5,7,9,12]
    result = list(map(lambda a : a*a , num_list))

    #print(result) - without list(map())
    #< map object at 0x00000210DA5DAD40 >

    print(result)
    #Output: [4, 25, 49, 81, 144]

    #Code2
    num1 = [1,3,5]
    num2 = [3,7,1]
    num3 = [5,4,2]

    result2 = list(map(lambda a,b,c : a+b+c, num1,num2,num3))

    print(result2)
    #Output : [9, 14, 8]
