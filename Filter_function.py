if __name__ == '__main__':

    #print if number is even
    def even_fun(a):
        return True if a%2 == 0 else False

    num = [i for i in range(1,11)]

    num_list = list(filter(even_fun, num))

    print(num_list)



