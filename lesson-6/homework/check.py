def check(func):
    def wrapper(a, b):
      try:
         return func(a, b)
      except ZeroDivisionError:
         print("Denominator can't be zero")
    return wrapper



@check
def div(a, b):
   return a / b

print(div(6, 2))