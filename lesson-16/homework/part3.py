import pandas as pd


def task1():
    df = pd.read_json("lesson-16/homework/data/iris.json")

    columns = list(df.columns)

    for i in range(len(columns) - 1):
        mean_value = df[columns[i]].mean()
        median_val = df[columns[i]].median()
        str_dev = df[columns[i]].std()
        print(columns[i])
        print(f"Mean Value: {mean_value}")
        print(f"Median Value: {median_val}")
        print(f"Standard devision: {str_dev}")

def task2():
    df = pd.read_excel("lesson-16/homework/data/titanic.xlsx")
    ages = df["Age"]
    min = ages.min()
    max = ages.max()
    sum = ages.sum()

    print(f"Min: {min}, Max: {max}, Sum: {sum}")
def task3():
    df = pd.read_csv("lesson-16/homework/data/movie.csv")
    likes = df["movie_facebook_likes"]
    index = likes.idxmax()
    max = likes.max()
    top = df.sort_values(by="movie_facebook_likes", ascending=False)[["director_name", "movie_facebook_likes"]].head(1)
    print(top)

    top_5_longest = df.sort_values(by="duration", ascending=False)[["duration", "director_name", "movie_title"]].head(5)
    print(top_5_longest)

    df = pd.read_parquet("lesson-16/homework/data/flights/part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet")
    df.fillna(df)
