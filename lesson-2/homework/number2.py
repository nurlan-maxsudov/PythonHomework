print("Enter 3 numbers: ")

num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
num3 = int(input("3rd number: "))

if (num1 > num2 and num1 > num3):
    print("Max: ",num1)
elif (num2 > num3):
    print("Max: ",num2)
else:
    print("Max: ",num3)

if (num1 < num2 and  num1 < num3):
    print("Min: ", num1)
elif (num2 < num3):
    print("Min: ", num2)
else:
    print("Min: ", num3)