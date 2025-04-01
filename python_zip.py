a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
x = tuple(x)

# for a, b in x:
    # print(a + b)
    
def print_numbers(*n):
    return n

print(print_numbers(*[1, 2, 3]))

print(print_numbers(1, 2, 3))

print(*[1, 2, 3])