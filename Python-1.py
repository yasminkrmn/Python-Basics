

# List
list_ = [1, 2, 3, 4]

# append() Function
list_.append(5)
# Out[5]: [1, 2, 3, 4, 5]

# range() Function
list_1 = list(range(10, 100, 8)) # start # end # step
# Out[3]: [10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]

# pop() Function
list_1.pop() # Remove last value (default last).
list_1.pop(2) # Remove value which is in selected index.

# remove() Function
list_1.remove(10) # Remove value selected (default last).

# index() Function
list_1.index(34) # Give index of selected value

# filter() Function
list_2 = list(range(1, 25, 3))
# [1, 4, 7, 10, 13, 16, 19, 22]
def odd_number(number):
    return number % 2 == 0

list(filter(odd_number,list_2))
# [4, 10, 16, 22]

# map() Function
def square(number):
    return number ** 2

list(map(square,list_2))
# [1, 16, 49, 100, 169, 256, 361, 484]

# enumerate() Function
list(enumerate(list_2))
# [(0, 1), (1, 4), (2, 7), (3, 10), (4, 13), (5, 16), (6, 19), (7, 22)]
list(enumerate(list_2, 1))
# [(1, 1), (2, 4), (3, 7), (4, 10), (5, 13), (6, 16), (7, 19), (8, 22)]

# sorted() Function
sorted('yasemin')
# ['a', 'e', 'i', 'm', 'n', 's', 'y']

# zip() Function

a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']

print(*zip(a1, a2))
# ('a', 'd') ('b', 'e') ('c', 'f')
list(zip(a1, a2))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]

names = ['Mary', 'Adam', 'Aden']
ages = [25, 40, 20]

for i, j in zip(names, ages):
    print('Name: {} - Age: {}'.format(i, j))

# Name: Mary - Age: 25
# Name: Adam - Age: 40
# Name: Aden - Age: 20