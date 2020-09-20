'''
Written: 20.09.2020
Author: Anton Kazakevich
Algorithm: Binary search for the arrays
Language: Python 3.x
'''

from random import randint, choice

min_int = 0 #Min integer that can be generated
max_int = 100 #Max integer that can be generated
lenght = 10 #Lenght of the array
arr = []
rand_int = randint(min_int, max_int)

#Filling the array with random integers 
for i in range(lenght):
	while rand_int in arr:
		rand_int = randint(0, max_int)
	arr.append(rand_int)

#Function of binary search
def binary_search(array, item):
	index = None #Index of item we need to find

	array = sorted(array) #Sorting array with the built-in fucntion

	print("Array - ", array)
	print("Need to find - ", item)

	#The boundaries of the area we are checking
	low = 0 
	high = len(array) - 1
	
	#Middle element of the area we are checking
	mid = (high + low) // 2 

	while True:
		if array[mid] == item: #We found item!
			index = mid
			break

		if array[mid] > item:
			high = mid - 1		
		elif array[mid] < item:
			low = mid + 1

		mid = (low + high) // 2

	return index


find_item = choice(arr) #Random element of the array (just for test)
find_index = binary_search(arr, find_item) #Need to return index of the element
print("Index of item - ", find_index) #Print this index