itr = 3
elements = [1, 3, 2, 5]

repeated_elements = []

for j in range(len(elements)):
    for i in range(itr):
            repeated_elements.append(elements[j])

print(repeated_elements)
