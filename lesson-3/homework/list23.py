elements = [1, 2, 3, 4, 5, 8, 1, 3, 4, 10, 9]

odd_numbers = []

for i in range(len(elements)):
    if elements[i] % 2 == 1:
        odd_numbers.append(elements[i])

print(odd_numbers)