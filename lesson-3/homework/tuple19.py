elements = (1, 2, 1, 4, 1, 3, 4, 2, 10)

element = 1

listed_elements = list(elements)

if element in listed_elements:
    listed_elements.remove(element)

tupled_elements = tuple(listed_elements)

print(tupled_elements)
