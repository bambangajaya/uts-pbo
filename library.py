class Library:

    def __init__(self):
        self.books = []
        self.borrowers = {}

    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
       for book in self.books:
        if book.rent == 0:
            print(f"{book}\nStatus: Available")
        else:
            print(f"{book}\nStatus: Borrowed by {book.borrower}. Due date: {book.due_date.strftime('%Y-%m-%d')}")


    def borrow_book(self, book_name, borrower):
        for book in self.books:
            if book.book_name == book_name:
                if book.rent < 1:
                    book.rent += 1
                    if book_name in self.borrowers:
                        self.borrowers[book_name].append(borrower)
                    else:
                        self.borrowers[book_name] = [borrower]
                    book.borrower = borrower
                    book.library = self
                    return f"{book_name} has been borrowed by {borrower}."
                else:
                    return f"{book_name} is already borrowed."
        return "The requested book is not available."
    
    def display_books(self):
        for book in self.books:
            print(book)

    def display_borrowers(self):
        for book_name, borrowers in self.borrowers.items():
            print(f"{book_name} has been borrowed by {', '.join(borrowers)}")