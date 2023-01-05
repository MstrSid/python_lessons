# Create two different (not copy) variables with type set and equals values
# User equal for check this two
# Use is for check this two
# Check have any value in sets

set_one = {1, 2, 3}
set_two = {1, 2, 3}
print(set_one.__eq__(set_two))
print(set_one is set_two)
print(1 in set_one)
