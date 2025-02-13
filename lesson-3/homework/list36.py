numbers = [10, -5, 23, -42, 56, -17, 89, -34, 67, -90]

positive_sum = 0
for i in range(len(numbers)):
    if numbers[i] > 0:
        positive_sum += numbers[i]
    
print(positive_sum)