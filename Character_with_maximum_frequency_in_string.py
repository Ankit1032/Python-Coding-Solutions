if __name__ in '__main__':

    s1 = "maryhasalittlelambsnowfallinthewinterrainyinsummer"

    freq_dict = {}

    for i in s1:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1

    # Sort the dict on keys
    for i in sorted(freq_dict.keys()):
        print(i, freq_dict[i])

    #Getting key with maximum value in dictionary
    #k = max(freq_dict,key=freq_dict.get)

    k = max(freq_dict,key= lambda x : freq_dict[x])

    print(k,"is the most occured letter in the string")
