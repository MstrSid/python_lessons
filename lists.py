# Task 1
# Create list with 5 mix types elements
# Remove 3thd element
# Print length list
# Change order element list
# Create another list with 2 elements
# Extend 1st list with elements from 2nd list
# Print extend 1st list
mixed_list = [1, 'a', True, 2.8, 3]
del mixed_list[2]
print(len(mixed_list))
mixed_list.reverse()
another_list = ['c', 'b']
mixed_list.extend(another_list)
print(mixed_list)

# Task 2
# Create 2 lists
# Concatenate two lists with + operator
# Say, what magick method using in operator +
# Concatenate two lists with this magick method

list_one = [1, 6, 3]
list_two = ['a', 'b', 'c']
common_list = list_one + list_two # magic method __add__
print(common_list)
new_common_list = list_one.__add__(list_two)
print(new_common_list)
