# Create empty dict
# Ask user input 3 key and 3 value for dict
# Add all info from user in dict
# Print resul dict
# Add custom key/value
# Delete key
# Print result

new_dict = {}
for i in range(0, 6):
    if (i % 2 == 0):
        key = input('input key: ')
        continue
    if i % 2 != 0:
        val = input('input value: ')
    new_dict[key] = val

print(new_dict)

new_dict['d'] = 18
print(new_dict)
del new_dict['d']
print(new_dict)
