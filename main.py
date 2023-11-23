from fastapi import FastAPI

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