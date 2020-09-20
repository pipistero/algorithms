'''
Written 20.09.2020
Author: Anton Kazakevich
Algorithm: Quick sort (good sort if pivot is good)
Language: Python 3.x
'''

from random import randint

max_int = 100 #Max integer that can be generated
lenght = 10 #Lenght of the array
arr = []
sorted_arr = []
rand_int = randint(0, max_int)

#Filling the array with random integers
for i in range(lenght):
	while rand_int in arr:
		rand_int = randint(0, max_int)
	arr.append(rand_int)

def qsort(array):
	l = len(array) #Lenght of the array
	if l <= 1: #Array already sorted, just return it
		return array
	else:
		rindex = randint(0, l - 1) #Index of the random element
		pivot = array[rindex] #Pivot = random element

		#Fiiling array with numbers that less than pivot
		less = [e for e in array if e <= pivot and array.index(e) != rindex]
		#Filling array with numbers that greater than pivot
		greater = [e for e in array if e > pivot and array.index(e) != rindex]

		#Return sorted array less, pivot and sorted array greater
		return qsort(less) + [pivot] + qsort(greater)

#Sorting the array
sorted_arr = qsort(arr)

#Printing the arrays
print(arr)
print(sorted_arr)