elements = (1, 2, 3, 4, 5, 8, 1, 3, 4, 10, 9)
unique_elements = []

for i in range(len(elements)):
    if elements[i] not in unique_elements:
        unique_elements.append(elements[i])

print(tuple(unique_elements))
