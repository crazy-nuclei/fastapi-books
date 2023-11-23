from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/")
def first_api():
    return {"message": "Hello AA !"}

@app.get("/books")
def get_books():
    return BOOKS

@app.get("/books/{book_title}")
def get_books(book_title: str):
    for book in BOOKS: 
        if book.get("title").casefold() == book_title.casefold():
            return book
    return {}

@app.get("/books/")
def get_books_by_category(category: str):
    books = []
    for book in BOOKS: 
        if book.get('category').casefold() == category.casefold():
            books.append(book)
    return books

@app.get("/books/{author}/")
def get_books_by_author_and_category(author: str, category: str):
    books = []
    for book in BOOKS: 
        if book.get('category').casefold() == category.casefold() and book.get("author").casefold() == author.casefold():
            books.append(book)
    return books

@app.post("/books")
def add_new_book(book=Body()):
    BOOKS.append(book)

@app.put("/books")
def update_book(book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book.get("title").casefold(): 
            BOOKS[i] = book

@app.delete("/books/{book_title}")
def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break