if __name__ == '__main__':

    #str1 = "Earth"
    #str2 = "heArT"

    str1 = "Ankit"
    str2 = "Ankita"
    
    str1 = sorted(str1.lower())
    str2 = sorted(str2.lower())

    if str1 == str2:
        print("The strings are anagram")
    else:
        print("The strings are not anagram")
