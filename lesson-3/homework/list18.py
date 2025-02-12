elements = [1, 2, 5, 6, 8, 1, 3, 4, 10]

sub_list = [2, 5, 11]

exists = True

for i in range(len(sub_list)):
    if sub_list[i] not in elements:
        exists = False

if exists:
    print("Sublist exists in the list")
else:
    print("Sublist does not exist in the list") 