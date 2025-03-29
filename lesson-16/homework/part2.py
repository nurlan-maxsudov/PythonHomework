import pandas as pd
from collections import Counter


def task1():
    df = pd.read_json("lesson-16/homework/data/iris.json")

    df.columns = df.columns.str.lower()

    df_selected = df[["sepallength", "sepalwidth"]]

    print(df_selected.head())

def task2():
    df = pd.read_excel("lesson-16\\homework\\data\\titanic.xlsx")
    filtered_df = df[df['Age'] > 30]
    print(filtered_df["Age"].head(10))

    gender = df["Sex"]

    value_counter = Counter(gender)
    print(value_counter)

def task3():
    df = pd.read_parquet("lesson-16/homework/data/flights/part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet")
    filtered_df = df[["Origin", "Dest"]]
    print(filtered_df)

    unique_dest = filtered_df["Dest"].unique()
    print(unique_dest)

def task4():
    df_movies = pd.read_csv("/lesson-16/homework/data/movie.csv")
    durations = df_movies[df_movies["duration"] > 120]

    sorted = df_movies['movie_facebook_likes'].sort_values(ascending=False)

    return durations, sorted
