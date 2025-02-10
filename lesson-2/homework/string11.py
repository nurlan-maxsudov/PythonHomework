digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

string = input("Enter a string: ")

for i in range(len(string)):
    if string[i] in digits:
        print("Found!")
        break