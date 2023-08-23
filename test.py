from sys import getsizeof
g1 = (i for i in range(1000000))
list1 = [i for i in range(1000000)]
print (getsizeof(g1))
print (getsizeof(list1))