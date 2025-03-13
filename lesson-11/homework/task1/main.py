import sqlite3

#1
def create_database():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        query = "Create table Roster(Name TEXT, Species TEXT, Age int)"
        cur.execute(query)

#2
def insert_data():
    values = """
        Insert into Roster Values
        ('Benjamin Sisko','Human',40),
        ('Jadzia Dax','Trill',300),
        ('Kira Nerys','Bajoran',29)
    """
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        cur.execute(values)

# 3
def update_data():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        cur.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")

#4
def query_data():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        query = "SELECT * from Roster WHERE Species = 'Bajoran'"
        data = cur.execute(query)
        info = data.fetchall()
        print(f"Name:{info[0][0]}, Species:{info[0][1]}")

#5
def delete_data():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        cur.execute("Delete from Roster where age>100")

#6
def add_column():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        
        # Add the Rank column
        cur.execute("ALTER TABLE Roster ADD column Rank TEXT")
        
        # Update the Rank values
        changes = """
        UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
        UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
        UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax';
        """
        cur.executescript(changes)

#7
def sort_data():
    with sqlite3.connect("roster.db") as connector:
        cur = connector.cursor()
        data = cur.execute("Select * from Roster order by Age desc")
        information = data.fetchall()
    for info in information:
        print(f"{info[0], info[1]}, {info[2]}, {info[3]}")

def main():
    create_database()
    insert_data()
    update_data()
    query_data()
    add_column()
    sort_data()
    delete_data()

if __name__ == "__main__":
    main()
    