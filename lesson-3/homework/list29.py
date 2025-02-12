numbers = [3, 1, 7, 9, 2, 6, 8]

index = 5


if index > len(numbers):
    print("Out of range")

else:
    numbers.remove(numbers[index])

print(numbers)
