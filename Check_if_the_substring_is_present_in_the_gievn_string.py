
if __name__ == '__main__':

    s1 = "My name is ankit banerjee"
    s2 = "name"

    #in
    if s2 in s1:
        print("present")
    else:
        print("absent")

    #find()
    print("absent") if s1.find(s2) == -1 else print("present")

    #index()
    try:
        s1.index(s2)
    except ValueError:
        print("ABSENT")
    else:
        print("PRESENT")
