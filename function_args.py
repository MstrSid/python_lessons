# Refactor call function from functions.py to arguments with keywords
# Refactor call function from functions.py to 1 positional args and 1 kayword
from copy import deepcopy


def merge_lists_to_dict(l1, l2):
    zip_item = zip(l1, l2)
    dictionary = dict(zip_item)
    return dictionary


list_one = ['a', 'b', 'c']
list_two = [1, 2, 3]
print(merge_lists_to_dict(l1=list_one, l2=list_two))
print(merge_lists_to_dict(list_one, l2=list_two))


# Create function update_car_info where args must add in dictionary
# Add new key is_available with value True
def update_car_info(**kwargs):
    car = deepcopy(kwargs)
    car['is_available'] = True
    return car


print(update_car_info(name='Mazda', model='626', price='2500'))
