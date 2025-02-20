def convert_cel_to_far(C):
    F = C * 9/5 + 32
    F = round(F, 2)

    return F

def convert_far_to_cel(F):
    C = (F - 32) * 5/9
    C = round(C, 2)
    return C

print("Enter a temperature in degrees F:", end= " ")
F = float(input())

print(f"{F} degrees F = {convert_far_to_cel(F)} degrees C")

print("Enter a temperature in degrees C:", end=" ")
C = float(input())

print(f"{C} in degrees C = {convert_cel_to_far(C)} degrees C")

