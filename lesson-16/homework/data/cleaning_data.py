import pandas as pd

df = pd.read_csv("data.csv")
#It does not change the original data
# To change the original data, we need to use "in_place=True"
new_df = df.dropna()

# print(new_df)

filled_data = df.fillna(77)
# print(df)
# print(filled_data)

#Filling specified columns

filled_data1 = df["Calories"].fillna(88)
# print(filled_data1)

#Mean, Median, Mode

x = df["Calories"].mean()
# print(df["Calories"].fillna(x))

y = df["Calories"].median()
# print(df["Calories"].fillna(y))

z = df["Calories"].mode()[0]
print(z)
print(y)