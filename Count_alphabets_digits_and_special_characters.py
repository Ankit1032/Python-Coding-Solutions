
if __name__ == '__main__':

    str = "ab@d1s5%deA43*"

    dict_char = {
        "alphabet" : 0,
        "digit" : 0,
        "special_char" : 0
    }

    for i in str:
        if i.isalpha():
            dict_char['alphabet'] = dict_char['alphabet'] + 1

        elif i.isdigit():
            dict_char['digit'] = dict_char['digit'] + 1

        else:
            dict_char['special_char'] = dict_char['special_char'] + 1

    print(dict_char)
