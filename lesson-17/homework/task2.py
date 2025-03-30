import pandas as pd
import pyarrow

def part1():

    df = pd.read_excel("lesson-17/data/titanic.xlsx")

    avg_age = df.groupby("Pclass")['Age'].mean()

    total_fare = df.groupby("Pclass")["Fare"].sum()

    new_dic = {
        "Average age": avg_age,
        "Total fare": total_fare
    }

    new_df = pd.DataFrame(new_dic)

    return new_df
def part2():
    df = pd.read_csv("lesson-17/data/movie.csv")
    print(df)

    grouped_df = df.groupby(["color", "director_name"]).agg({
        "num_critic_for_reviews": "sum",
        "duration": "mean"
    })

    grouped = grouped_df.reset_index()
    print(grouped)
    
def part3():
    df = pd.read_parquet("lesson-17\data\\flights\part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet")
    df['ArrDelay'] = pd.to_numeric(df['ArrDelay'], errors='coerce')
    df['DepDelay'] = pd.to_numeric(df['DepDelay'], errors='coerce')
    grouped_df = df.groupby(["Year", "Month"]).agg(
        AvgDelay = ('ArrDelay', 'mean'),
        MaxDelay =  ('DepDelay', 'max')
        )


    print(grouped_df)