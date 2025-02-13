numbers = [2, 3, 1, 4, 5, 1, 2, 9, 10]

sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cur_num = numbers[0]

ascending = True

for i in range(1, len(sorted_numbers)):
    if sorted_numbers[i] < cur_num:
        ascending = False
    cur_num = sorted_numbers[i]
    
if ascending:
    print("It is sorted")
else:
    print("It is not sorted")