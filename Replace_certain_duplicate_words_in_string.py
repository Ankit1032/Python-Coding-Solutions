if __name__ == '__main__':

    ori_str = 'Gfg is best . Gfg also has Classes now. Classes help understand better.'

    # printing original string
    print("The original string is : " + str(ori_str))

    # initializing replace mapping
    repl_dict = {'Gfg': 'It', 'Classes': 'They'}

    str_list = list(ori_str.split(" "))
    #print(str_list)

    dub_dict = {}

    for index,j in enumerate(str_list):
        if j not in dub_dict:
            dub_dict[j] = 1
        else:
            str_list[index] = repl_dict[j]


    print("AFTER REPLACING =====")
    print(' '.join(str_list))



