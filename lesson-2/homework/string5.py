string = input().lower()

num_vowel = 0
num_consonant = 0

for i in range(len(string)):
    if string[i] in "aeiou":
        num_vowel += 1
    else:
        num_consonant += 1

print(num_vowel)
print(num_consonant)