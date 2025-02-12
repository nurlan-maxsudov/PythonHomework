elements = [1, 2, 3, 4, 5, 8, 1, 3, 4, 10, 9, 11]

length = len(elements)

if length % 2 == 0:
    print(elements[length // 2 - 1], elements[length // 2])
else:
    print(elements[length // 2])
