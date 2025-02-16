keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

length = len(keys)

dic = {}

for i in range(length):
    dic[keys[i]] = values[i]

print(dic)