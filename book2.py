from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    id: Optional[int] = Field(description='ID not needed on creation', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=2)
    description: str = Field(min_length=1, max_length=200)
    rating: int = Field(gt=0, lt=6)

    model_config = {
        'json_schema_extra': {
            'example': {
                'title': 'rufai and python',
                'author': 'abdul-mumin rufai',
                'description': 'i want to be a AI/ML engineer',
                'rating': 5
            }
        }
    }


BOOKS = [
    Book(1, 'computer science', 'Abdul-Mumin', 'I love programming', 5),
    Book(2, 'calculus', 'Abdul-Mumin', 'calculus is good', 5),
    Book(3, 'linear algebra', 'Abdul-Mumin', 'it good for recommender systems', 5),
    Book(4, 'economics', 'Author One', 'something good', 4),
    Book(5, 'geography', 'Author Two', 'Earth is not flat', 3),

]


@app.get('/books')
def get_all_books():
    return


@app.get('/books/{book_id}')
async def get_book_id(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.post('/books/create_book')
async def add_book(new_book: CreateBook):
    book = Book(**new_book.dict())  # the ** is helping to create property value pairs in the dictionary
    BOOKS.append(is_book_id(book))


def is_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book
