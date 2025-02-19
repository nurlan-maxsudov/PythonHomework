password = input("Create a password: ")

is_all_lower = True
    
for i in range(len(password)):
    if password[i].isupper():
        is_all_lower = False

if len(password) < 8:
    print("The password is too short!")

if is_all_lower:
    print("Password should contain at least one uppercase letter")
    