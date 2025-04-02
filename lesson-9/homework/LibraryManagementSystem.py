class BookNotFoundException(Exception):
    def __init__(self):
        super().__init__(self)

class BookAlreadyBorrowedException(Exception):
    def __init__(self):
        super().__init__(self)

class MemberLimitExceededException(Exception):
    def __init__(self):
        super().__init__(self)

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} - {status}"
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

class Member:
    def __init__(self, name, borrowed_books=None):
        if borrowed_books is None:
            borrowed_books = []
        self.name = name
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f"{self.name}"

    def can_borrow_more(self):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException()
        return True
        
    def __eq__(self, other):
        if isinstance(other, Member):
            return self.name == other.name
        return False

class Library:
    def __init__(self, books=None, members=None):
        if books is None:
            books = []
        if members is None:
            members = []
        self.books = books
        self.members = members

    def add_book(self, book: Book):
        if book in self.books:
            print("Book already exists")
        else:
            self.books.append(book)
            print("Book added successfully!")

    def add_member(self, member: Member):
        if member in self.members:
            print("Member already exists")
        else:
            self.members.append(member)
            print("Member added successfully!")

    def borrow_book(self, title: str, member: Member):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed:
                    raise BookAlreadyBorrowedException()
                member.borrowed_books.append(book)
                book.is_borrowed = True
                print("Book borrowed successfully!")
                return
        raise BookNotFoundException()

    def return_book(self, title: str, member: Member):
        book_to_return = next((b for b in member.borrowed_books if b.title == title), None)
        if book_to_return:
            member.borrowed_books.remove(book_to_return)
            book_to_return.is_borrowed = False
            print("Book returned successfully!")
            return
        raise BookNotFoundException()

def main():
    initial_books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee")
    ]
    initial_members = [
        Member("Alice"),
        Member("Bob"),
        Member("Charlie")
    ]
    lib = Library(initial_books, initial_members)  
    print("You have 7 options:")
    print("1. Add book")
    print("2. Add member")
    print("3. See all books")
    print("4. See all members")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Exit")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name_of_book = input("Enter the name of book: ")
            author_of_book = input("Enter the author of the book: ")
            new_book = Book(name_of_book, author_of_book)
            lib.add_book(new_book)
        elif choice == 2:
            name_of_member = input("Enter the name of member: ")
            new_member = Member(name_of_member)
            lib.add_member(new_member)
        elif choice == 3:
            for book in lib.books:
                print(str(book))
        elif choice == 4:
            for member in lib.members:
                print(str(member))
        elif choice == 5:
            member_name = input("Enter your name: ")
            member = next((m for m in lib.members if m.name == member_name), None)
            if member:
                try:
                    member.can_borrow_more()
                    book_title = input("Enter the title of the book you want to borrow: ")
                    lib.borrow_book(book_title, member)
                except MemberLimitExceededException:
                    print("You cannot borrow more than 3 books.")
                except BookAlreadyBorrowedException:
                    print("This book is already borrowed.")
                except BookNotFoundException:
                    print("This book is not available in the library.")
            else:
                print("Member not found.")
        elif choice == 6:
            member_name = input("Enter your name: ")
            member = next((m for m in lib.members if m.name == member_name), None)
            if member:
                book_title = input("Enter the title of the book you want to return: ")
                try:
                    lib.return_book(book_title, member)
                except BookNotFoundException:
                    print("This book is not found in the library.")
            else:
                print("Member not found.")
        elif choice == 7:
            break

if __name__ == "__main__":
    main()