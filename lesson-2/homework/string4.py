original_str = input()

reversed_str = original_str[::-1]

if original_str == reversed_str:
    print("Palindrome")
else:
    print("Not palindrome")