def find_duplicate(array):

    num_set = set()

    for i in range(len(array)):
        if array[i] in num_set:
            return array[i]
        else:
            num_set.add(array[i])

array = print(find_duplicate([1, 2, 3, 4, 4, 5]))
