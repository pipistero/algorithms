'''
Written 20.09.2020
Author: Anton Kazakevich
Algorithm: VERY bad sort :)
Language: Python 3.x
'''

from random import randint

max_int = 100 #Max int that can be generated
lenght = 10 #Lenght of the array
arr = []
sorted_arr = []
rand_int = randint(0, max_int)

#Filling the array with random integers
for i in range(lenght):
	while rand_int in arr:
		rand_int = randint(0, max_int)
	arr.append(rand_int)

#Sorting the array
for i in range(lenght):
	e_min = min(arr)
	index_min = arr.index(e_min)
	sorted_arr.append(arr.pop(index_min))

#Printing the arrays
print("Array before sort - "arr)
print("Array after sort - "sorted_arr)


