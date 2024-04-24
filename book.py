from datetime import datetime , timedelta # Langkah 1: Impor modul datetime

class Book:
    def __init__(self, book_name, author, year, rent=0, detail=""):
        self.book_name = book_name
        self.author = author
        self.year = year
        self.rent = rent
        self.detail = detail
        self.borrower = None
        self.borrow_date = None
        self.due_date = None
    def __str__(self):
        return f"Title: {self.book_name}\nAuthor: {self.author}\nYear: {self.year}\nRent Count: {self.rent}\nDetail: {self.detail}\n"

    def borrow_book(self, borrower):
        if self.rent < 1:
            self.rent += 1
            self.borrower = borrower
            self.borrow_date = datetime.now()  # Langkah 3: Atur borrow_date menjadi tanggal saat ini
            return f"{self.book_name} has been borrowed by {borrower} on {self.borrow_date}."
        else:
            return f"{self.book_name} is already borrowed."

    def return_book(self):
        self.rent -= 1
        if self.rent == 0:
            if self.book_name in self.library.borrowers:
                self.library.borrowers[self.book_name].remove(self.borrower)
                if not self.library.borrowers[self.book_name]:
                    del self.library.borrowers[self.book_name]
        return f"{self.book_name} has been returned."
