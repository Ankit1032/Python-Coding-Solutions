
if __name__ == '__main__':

    str = "My Name is Ankit Banerjee"

    #String is immutable so make a new string variable

    str_new = ""
    dict_new = {}

    for i in str:
        if i not in dict_new.keys():
            dict_new[i] = 1

    for i in dict_new.keys():
        str_new = str_new + i

    print(str_new)
