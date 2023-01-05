# Create function merge_lists_to_dict with 2 parameters
# Function must concatenate two lists, using zip
# Convert zip object to dictionary and return it from function
def merge_lists_to_dict(l1, l2):
    zip_item = zip(l1, l2)
    dictionary = dict(zip_item)
    return dictionary


list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
print(merge_lists_to_dict(list_one, list_two))
