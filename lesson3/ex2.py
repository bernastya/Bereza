from book import Book

library = [
    Book("Война и мир", "Толстой"),
    Book("Преступление и наказание", "Достоевский"),
    Book("Мастер и Маргарита", "Булгаков")
]

for book in library:
    print(f"{book.title} - {book.Author}")
