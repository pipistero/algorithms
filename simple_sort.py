'''
Written 20.09.2020
Author: Anton Kazakevich
Algorithm: VERY bad sort :)
Laguage: Python 3.x
'''

from random import randint

min_int = 0 #Min integer that can be generated
max_int = 100 #Max intteger that can be generated
lenght = 10 #Lenght of the array
arr = []
sorted_arr = []
rand_int = randint(0, max_int)

#Filling the array with random integers
for i in range(lenght):
	while rand_int in arr:
		rand_int = randint(min_int, max_int)
	arr.append(rand_int)


#Printing the array
print("Array before sort - ", arr)

#Sorting the array
for i in range(lenght):
	e_min = min(arr)
	index_min = arr.index(e_min)
	sorted_arr.append(arr.pop(index_min))

#Printing the array
print("Array after sort - ", sorted_arr)
