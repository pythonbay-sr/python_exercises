"""
Link : https://www.w3resource.com/python-exercises/array/
Text : Write a Python function that takes two lists and returns True if they have at least one common member
"""


my_list = ("banana", "car", "phone", "speakers", "flag")
my_list_2 = ("computer", "house", "school", "picture", "flag")


if  len(my_list)>len(my_list_2):
    longest=my_list
    shortest=my_list_2
else:
    longest=my_list_2
    shortest=my_list


for i in range(len(longest)):
    if longest[i] in shortest:
        print(longest[i])
    else:
        pass
