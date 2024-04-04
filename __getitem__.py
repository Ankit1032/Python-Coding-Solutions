# __getitem__ mathod allows us to buld our own data structure that can respond similar to a array or dictionary.
# It allows you to access elements of an object, like a list or a custom class using square brackets
# Here we are going to make our own array

# class Array:
#     def __init__(self) -> None:
#         self.items = ['item']
#
#     def __getitem__(self,key):
#         print(key)
#         return self.items[key]
#
# a = Array()
# print(a[0])
# #a['a']

# below is how list in python works when you assign mylist=[1,2,3] and then access mylist[1]
class MyList:
    def __init__(self):
        self.data = [1,2,3]

    def __getitem__(self,index):
        return self.data[index]

mylist = MyList()
print(mylist[1])