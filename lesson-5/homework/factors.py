def factors(n):
    for i in range(1, n+1):

        if (n % i == 0):
            print(f"{i} is a factor of {n}")

factors(12)