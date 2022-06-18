

if __name__ == '__main__':

    test_dict = {
        'A':5,
        'B': 1,
        'I': 6,
        'D': 9,
        'F': 2,
    }

    #sort the dictionary keys
    print(sorted(test_dict.keys()))

    # sort the dictionary values
    print(sorted(test_dict.values()))
    #print(sorted(test_dict, key=lambda a: test_dict[a])) XXXXX wrong (find out why?)

    # sort the dictionary by keys
    print(sorted(test_dict.items()))

    # sort the dictionary by values
    print(sorted(test_dict.items() , key = lambda i : i[1]))
