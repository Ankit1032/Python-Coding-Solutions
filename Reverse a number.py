if __name__ == '__main__':
    num = int(input("Enter a number: "))

    # rev_num = 0
    # #Non pythonic way
    # while num != 0:
    #     rev_num = int(rev_num*10 + num%10)
    #     num = int(num/10)


    #print(rev_num)

    #pythonic way
    print(str(num)[::-1])
