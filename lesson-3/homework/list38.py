numbers = [1, 2, 3, 4, 4, 4, 3, 2, 1]

left_index = 0
right_index = len(numbers) - 1

is_palindrome = True

while left_index < right_index:
    if numbers[left_index] != numbers[right_index]:
        is_palindrome = False
        break
    left_index += 1
    right_index -= 1

if is_palindrome:
    print("It is palindrome")
else:
    print("It is not palindrome")