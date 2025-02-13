numbers = [10, -5, 23, -42, 56, -17, 89, -34, 67, -90]

negative_sum = 0
for i in range(len(numbers)):
    if numbers[i] < 0:
        negative_sum += numbers[i]
    
print(negative_sum)