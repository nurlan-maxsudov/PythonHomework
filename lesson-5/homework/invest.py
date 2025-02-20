def invest(amount, rate, years):
    for i in range(years):
        amount += amount*rate

        print(f"year {i+1}: {round(amount, 2)}")
    
    

invest(100, .05, 4)