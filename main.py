from book import Book
import library
import search

# Add some books to the library for demonstration purposes
my_library = library.Library()
my_library.add_book(Book("maind set","Eric", "2011", detail="buku ini berisikan bagaimana mengatur pikiran atau ide untuk mengggapai suatu hall dengan benar dan terbaik"))
my_library.add_book(Book("investasi and saham","Brian lim ", "2020", detail="buku ini berisi tentang bagaimana caranya belajar saham dan belajar investasi dengan benar."))
my_library.add_book(Book("laskar pelangi", " Andrea Hirata ", "2005", detail="Novel ini bercerita tentang kehidupan 10 anak dari keluarga miskin yang bersekolah (SD dan SMP) di sebuah sekolah Muhammadiyah di Belitung yang penuh dengan keterbatasan."))
my_library.add_book(Book("apa arti kehidupan","Hulbert", "2015", detail="buku tentang kehidupan yang sangat berarti dan dapat merubah kehidupan."))
my_library.add_book(Book("si kancil","jameswl", "2017", detail="kisah cerita rakyar tentang kancil yang sangat pintar"))

# Driver Code
if __name__ == "__main__":

    print("=========== WELCOME TO ukrida E-LIBRARY ===========")
    print('''
          1. list book
          2. borrow book
          3. return book 
          4. search for a book 
          5. List the count of books in the library
          6. List borrowers 
          7. Exit
           ''')


    while True:
        input_choice = input("Enter one of the above: ")

        if input_choice == '1':
            print("Here are the books currently available in the library:")
            my_library.display_books()
        elif input_choice == '2':
            book_name = input("Enter the book name you want to borrow: ")
            borrower = input("Enter the borrower's name: ")
            print(my_library.borrow_book(book_name, borrower))
        elif input_choice == '3':
            book_name = input("Enter the book name you want to return: ")
            for book in my_library.books:
                if book.book_name == book_name:
                    print(book.return_book())
        if input_choice == '4':
            keyword = input("Enter the book name: ")
            print("search result:")
            search.search_books(keyword, my_library)
        elif input_choice == '5':
            print(f"There are {len(my_library.books)} books in the library.")
        elif input_choice == '6':
            print("Here are the borrowers:")
            print(my_library.display_borrowers())
        elif input_choice == '7':
            print("Thank you for using the library.")
            break
        else:
            print("Invalid choice. Please enter one of the above.")