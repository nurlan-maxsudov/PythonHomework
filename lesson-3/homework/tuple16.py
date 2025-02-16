elements = (1, 2, 1, 4, 1, 3, 4, 2, 10)

current_element = elements[0]

is_sorted = True
for i in range(1, len(elements)):
    if current_element > elements[i]:
        is_sorted = False
        break
    current_element = elements[i]

if is_sorted:
    print("The tuple is sorted")
else:
    print("The tuple is not sorted")