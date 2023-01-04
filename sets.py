# Create set with misc type element
# Add one element in this set
# Add another set with elements, same of that elements must be same as in first set
# Find common element in two sets and save it in new set
# Convert common set in list and print it
set_a = {'a', 2, True}
set_a.add(4.8)
set_b = {4.8, 2, True, 'b'}
common_set = set_a.union(set_b)
res = list(common_set)
print(res)
