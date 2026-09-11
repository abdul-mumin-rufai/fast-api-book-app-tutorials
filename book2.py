from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


# pydantic is a data validation libray use to validate data during development
class CreateBook(BaseModel):  # create book type
    id: int
    title: str
    author: str
    description: str
    rating: int


BOOKS = [
    Book(1, 'computer science', 'Abdul-Mumin', 'I love programming', 5),
    Book(2, 'calculus', 'Abdul-Mumin', 'calculus is good', 5),
    Book(3, 'linear algebra', 'Abdul-Mumin', 'it good for recommender systems', 5),
    Book(4, 'economics', 'Author One', 'something good', 4),
    Book(5, 'geography', 'Author Two', 'Earth is not flat', 3),

]


@app.get('/books')
def get_all_books():
    return BOOKS


@app.post('/books/create_book')
async def add_book(new_book: CreateBook):
    book = Book(**new_book.dict())  # the ** is helping to create property value pairs in the dictionary
    BOOKS.append(book)
