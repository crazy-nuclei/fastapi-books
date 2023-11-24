from fastapi import Body, FastAPI, Path, Query, HTTPException, status
from models.Book import Book
from pydantic_models.Book import BookPost

app = FastAPI()

BOOKS = [
    Book(1, 'Title One', 'Author One', 'description one', 1),
    Book(2, 'Title Two', 'Author Two', 'description Two', 2),
    Book(3, 'Title Three', 'Author Three', 'description Three', 3),
    Book(4, 'Title Four', 'Author Four', 'description Four', 4),
    Book(5, 'Title Five', 'Author Five', 'description Five', 5)
]

@app.get("/")
def first_api():
    return {"message": "Hello AA !"}

@app.get("/books")
def get_books():
    return BOOKS

@app.get("/books/author")
def get_books_by_author(author: str):
    books = []
    for book in BOOKS: 
        if book.get("author").casefold() == author.casefold():
            books.append(book)
    return books

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int = Path(gt=0)):
    for book in BOOKS: 
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/books/")
def get_books_by_rating(rating: int = Query(ge=1, le=5)):
    books = []
    for book in BOOKS: 
        if book.rating == rating:
            books.append(book)
    return books

@app.get("/books/{author}/")
def get_books_by_author_and_category(author: str, category: str):
    books = []
    for book in BOOKS: 
        if book.get('category').casefold() == category.casefold() and book.get("author").casefold() == author.casefold():
            books.append(book)
    return books

@app.post("/books", status_code = status.HTTP_201_CREATED)
def add_new_book(book: BookPost):
    new_book = Book(**book.model_dump())
    BOOKS.append(new_book)

@app.put("/books", status_code = status.HTTP_204_NO_CONTENT)
def update_book(book: BookPost):
    change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id: 
            BOOKS[i] = book
            change = True
            break
    if change != True: 
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/books/{book_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int):
    change = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            change = True
            break
    if change != True: 
        raise HTTPException(status_code=404, detail="Item not found")