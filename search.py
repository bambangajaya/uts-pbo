import library

def search_books(keyword, library):
    # Filter the library based on the keyword
    results = [book for book in library.books if keyword.lower() in book.book_name.lower() or keyword.lower() in book.author.lower()]

    # Print the results
    for result in results:
        print(result)
        print(f"Title: {result.book_name}, Author: {result.author}, Details: {result.detail}")
        