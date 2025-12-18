old_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {}
for key in old_dict:
    val = old_dict[key]
    new_dict[val] = key
print(new_dict)