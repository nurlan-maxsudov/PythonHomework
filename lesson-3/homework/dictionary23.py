dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
dict2 = {"b": 20, "c": 30, "d": 40, "e": 50}

keys1 = dict1.keys()
keys2 = dict2.keys()

is_in = False

for key in keys1:
    if key in keys2:
        is_in = True

if is_in:
    print("Common")
else:
    print("Not common")