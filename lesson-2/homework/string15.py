string = input()

words = string.split()

for word in words:
    print(word[0].upper(), end="")