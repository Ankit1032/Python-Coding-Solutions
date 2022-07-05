if __name__ == '__main__':

    num = int(input("Enter a number: "))
    array = [9,6,0,4,2,3,5,1,8,7]

    array.sort()
    print(array)
    start = 0
    end = len(array)-1

    present = False

    while(start<=end):
        mid = int((start+end)/2)

        if(array[mid] == num):
            print("{} is present".format(num))
            present = True
            break

        elif(num < array[mid]):
            end = mid-1
        else:
            start=mid+1

    if(present == False):
        print("{} is not present".format(num))
