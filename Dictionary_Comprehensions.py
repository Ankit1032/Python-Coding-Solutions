if __name__ == '__main__':

    #code1
    stocks = ['reliance', 'infosys', 'tcs']
    prices = [2175, 1127, 2750]
    stock_dict = {s:p for s,p in zip(stocks,prices)}
    print(stock_dict)
    #Output : {'reliance': 2175, 'infosys': 1127, 'tcs': 2750}

    #code2 (square)
    num = [1,2,3,4,5]
    num_dict = {x:x**x for x in num}
    print(num)
    #Output : [1, 2, 3, 4, 5]
