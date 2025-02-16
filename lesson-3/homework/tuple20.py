elements = (1, 2, 1, 4, 1, 3, 4, 2, 10)

listed_elements = list(elements)



subtuple1 = tuple(listed_elements[:3])
subtuple2 = tuple(listed_elements[3:6])

nested_tuple = (subtuple1, subtuple2)

print(nested_tuple)