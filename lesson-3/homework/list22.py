elements = [1, 2, 3, 4, 5, 8, 1, 3, 4, 10, 9]

even_numbers = []

for i in range(len(elements)):
    if elements[i] % 2 == 0:
        even_numbers.append(elements[i])

print(even_numbers)