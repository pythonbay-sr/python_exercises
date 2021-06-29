array = [1, 3, 5, 3, 7, 1, 9, 3]
reversed_array = []

length = len(array)


for i in range(len(array)):
               num = array[-1] #take a last number from the array
               del array[-1] #delete it
               reversed_array.append(num) #add it to the new array
print(reversed_array) #print a reversed array
