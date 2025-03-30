import sqlite3
import pandas as pd

def part1():
    conn = sqlite3.connect("lesson-17\data\chinook.db")

    customers = pd.read_sql("SELECT * FROM customers", conn)
    invoices = pd.read_sql("SELECT * FROM invoices", conn)

    merged_df = customers.merge(invoices, on="CustomerId", how="inner")

    invoice_counts = merged_df.groupby(["CustomerId", "FirstName", "LastName"]).size().reset_index(name="TotalInvoices")

    print(invoice_counts)

    conn.close()
def part2():
    df = pd.read_csv("lesson-17\data\movie.csv")

    df1 = df[["color", "director_name"]]
    df2 = df[["director_name", "num_critic_for_reviews"]]

    left_join_df = pd.merge(df1, df2, on="director_name", how="left")

    outer_join_df = pd.merge(df1, df2, on="director_name", how="outer")


    left_rows = left_join_df.shape[0]
    right_rows = outer_join_df.shape[0]
    print(left_rows, right_rows)

