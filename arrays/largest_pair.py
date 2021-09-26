"""
Link : https://www.w3resource.com/python-exercises/array/
Text : Write a Python program to find a pair with highest product from a given array of integers.
        Original array: [1, 2, 3, 4, 7, 0, 8, 4]
        Maximum product pair is: (7, 8)
        Original array: [0, -1, -2, -4, 5, 0, -6]
        Maximum product pair is: (-4, -6)
"""

array = [1, 2, 3, 4, 7, 0, 8, 4] #An example of an array

max = array[0]
max_2 = array[0]


for i in range(len(array)): #Find the largest number (max)
    if array[i]>max:
        max = array[i]

print(max) #Print the largest number

array.remove(max)

for i in range(len(array)): #Find the second largest number (max_2)
    if array[i]>max_2:
        max_2 = array[i]

print(max_2) #Print the second largest number
