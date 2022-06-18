if __name__ == '__main__':
    dict1 = {'a': 10, 'b': 8}
    dict2 = {'d': 6, 'c': 4, 'ss': [1, 2, 3]}

    dict1.update(dict2)

    print(sorted(dict1.items()))
