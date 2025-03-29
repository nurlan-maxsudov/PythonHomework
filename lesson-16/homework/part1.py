import pandas as pd
import sqlite3

def task1():
    conn = sqlite3.connect("lesson-16\homework\data\chinook.db")

    df_customers = pd.read_sql("SELECT * FROM customers", conn)

    print(df_customers.head(10))

    conn.close()

def task2():
    df_json = pd.read_json("lesson-16/homework/data/iris.json")

    print(df_json.shape)
    print(df_json.columns)

def task3():
    df_excel = pd.read_excel("lesson-16/homework/data/titanic.xlsx")
    print(df_excel.head())

def task4():
    df_parquet = pd.read_parquet("lesson-16/homework/data/flights/part-00000-aefaf364-d401-4e57-92a5-82fae6fdc855-c000.snappy.parquet")
    print(df_parquet.info())

def task5():
    df_csv = pd.read_csv("lesson-16/homework/data/movie.csv")
    print(df_csv.sample(10))

