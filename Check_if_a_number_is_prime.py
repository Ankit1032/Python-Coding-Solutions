import math

if __name__ == '__main__':

    num = int(input("Enter a number: "))
    #print(type(num))

    factors = 0
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            factors = factors+1


    if factors <= 1:
        print(num," is a prime number")
    else:
        print(num," is not a prime number")
