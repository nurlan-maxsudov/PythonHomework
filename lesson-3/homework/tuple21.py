elements = (1, 2, 3, 4, 5, 6)

itr = 3

list_elements = []

for i in range(len(elements)):
    for j in range(itr):
        list_elements.append(elements[i])
    
print(tuple(list_elements))