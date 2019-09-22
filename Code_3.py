# program to manipulate a list, arrays, matrix using numpy and inbuilt python functions
# Some handy inbuilt functions for list manipulation are:
# list.append()
# list.pop()
# list.insert()
# list.index()
# Some crucial numpy operations are:
# np.square(), np.sum(), np.exp(), np.sum(), np.ones(), np.zeros(), np.random.random() and much more

############ Part 1 - Integer list manipulation##########

num = [1,2,3,4,5,6,7,4]

# check whether a number is in the list or not
print(2 in num)

# add an element to the end of the list
num.append(11)
print(num)

# remove the last element from the list
num.pop()
print(num)

# remove the element from a specified index
num.pop(0)
print(num)

# add an element at the specified index
num.insert(0, 1)
print(num)

# find the index of an element
print(num.index(2))