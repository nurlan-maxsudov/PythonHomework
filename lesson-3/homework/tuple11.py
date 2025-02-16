elements = (1, 2, 1, 4, 1, 3, 4, 2, 10)

for i in range(len(elements)):
    if elements[i] == 1:
        print(i)

#or we can use more pythonic way by using list comprehension and enumrate method

indices = [index for index, value in enumerate(elements) if value == 1]

print(indices)