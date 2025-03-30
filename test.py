def uncommon_elements(list1, list2):
    new_list = []
    for num in list2:
        if num not in list1:
            new_list.append(num)
    
    for num in list1:
        if num not in list2:
            new_list.append(num)
    
    return new_list

list1 = [1, 1, 2]
list2 = [2, 3, 4]


print(uncommon_elements(list1, list2))

