class Person:
    def __init__(self, name: str, age: int):
        self.age = age
        self.name = name
        
    def is_adult(self):
        if self.age < 18:
            return False
        return True
    
import numpy as np

import pandas as pd

def add_age_column(df):
    df["Age in 5 years"] = df["Age"] + 5
    return df

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
df = add_age_column(df)
print(df)

def filter_even(numbers: list):
    for num in numbers:
        if num % 2 == 1:
            numbers.remove(num)
    return numbers

print(filter_even([1, 2, 3, 4, 5, 6]))  

