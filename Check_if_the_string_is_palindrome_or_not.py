
if __name__ == '__main__':

    str_res = input("Enter String: ")

    print("String is palindrome") if str_res == str_res[::-1] else print("String is not palindrome")


    #Check palindrome using .join and reversed()
    #The reversed() function returns the reversed iterator of the given sequence.
    print("checking palindrome using join and reversed")
    rev_str_res = "".join(reversed(str_res))
    if str_res == rev_str_res:
        print("String is palindrome")
    else:
        print("String is not palindrome")

