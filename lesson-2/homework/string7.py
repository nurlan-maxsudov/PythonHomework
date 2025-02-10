print("Input sentence:", end=" ")
string = input()
print("Replace:", end=" ")
word = input()
print("With:", end=" ")
to_replace = input()

new_string = string.replace(word, to_replace)

print(new_string)