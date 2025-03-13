import sqlite3

#1
def create_database():
    with sqlite3.connect("library.db") as connector:
        cur = connector.cursor()
        query = "Create table Books(Title TEXT, Author TEXT, Year_Published int, Genre TEXT)"
        cur.execute(query)

#2
def insert_data():
    with sqlite3.connect("library.db") as connector:
        cur = connector.cursor()   
        books = [
            ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
            ("1984", "George Orwell", 1949, "Dystopian"),
            ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
        ]
        
        cur.executemany("INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)", books)

#3
def update_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    conn.commit()
    conn.close()

#4
def query_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    results = cursor.fetchall()
    
    print("Dystopian Books:")
    for row in results:
        print(row)
    
    conn.close()

#5
def delete_data():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    conn.commit()
    conn.close()

#6
def add_rating_column():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    conn.commit()
    conn.close()

def update_ratings():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    ratings = {
        "To Kill a Mockingbird": 4.8,
        "1984": 4.7,
        "The Great Gatsby": 4.5
    }
    
    for title, rating in ratings.items():
        cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))
    
    conn.commit()
    conn.close()

#7
def advanced_query():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    results = cursor.fetchall()
    
    print("Books sorted by Year Published:")
    for row in results:
        print(row)
    
    conn.close()

def main():
    create_database()
    insert_data()
    update_data()
    query_data()
    delete_data()
    add_rating_column()
    update_ratings()
    advanced_query()
    
if __name__ == "__main__":
    main()