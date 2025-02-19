def uncommon_elements(list1, list2):
    for i in range(len(list2)):
        if list2[i] not in list1:
            list1.append(list2[i])
    
    return list1

list1 = [1, 1, 2]
list2 = [2, 3, 4]


print(uncommon_elements(list1, list2))

