elements = [1, 2, 3, 4, 5, 8, 1, 3, 4, 10, 9]

even_counter = 0

for i in range(len(elements)):
    if elements[i] % 2 == 0:
        even_counter += 1

print(even_counter)