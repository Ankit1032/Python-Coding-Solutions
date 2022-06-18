if __name__ in '__main__':
    s1 = "geeks for geeks is one of the leading websites of the world"

    l1 = list(s1.split(" "))

    word_freq = {}

    for w in l1:
        if w not in word_freq:
            word_freq[w] = 1
        else:
            word_freq[w] = word_freq[w] + 1

    #SOLUTION 1
    #final_str = ""
    # for i in word_freq:
    #     final_str = final_str + " " + i

    #SOLUTION 2
    final_str = " ".join(word_freq.keys())

    print(final_str)

