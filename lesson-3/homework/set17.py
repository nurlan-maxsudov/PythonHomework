set2 = {2, 1, 3, 6, 7}

set1 = set()

for i in set2:
    if i % 2 == 1:
        set1.add(i)

print(set1)