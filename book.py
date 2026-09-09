from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'name': 'Abdul-Mumin', 'author': 'Author One', 'category': 'Computing'},
    {'name': 'Abdul-Mumin', 'author': 'Author One', 'category': 'Computing'},
    {'name': 'Rufai-Bawa', 'author': 'Author Three', 'category': 'Economics'},
    {'name': 'Rukayatu-Yakubu', 'author': 'Author Four', 'category': 'Geography'},
    {'name': 'Bintu-Bawa', 'author': 'Author Five', 'category': 'Calculus'},
    {'name': 'Abdul-Mumin', 'author': 'Author Six', 'category': 'Economics'},
    {'name': 'Tijani-Yakubu', 'author': 'Author Seven', 'category': 'Maths'},
    {'name': 'Fatawu-Yakubu', 'author': 'Author Eight', 'category': 'English'},

]


@app.get('/books')
async def books():
    return BOOKS


@app.get('/books/mybook')
async def books():
    return {'book': 'this is my favourite book'}


# dynamic params must come after the static params
@app.get('/books/{name}')
async def books(name: str):
    for book in BOOKS:
        if book.get('name').casefold() == name.casefold():  # change to lower case letters because the url is lower
            # case
            return book


@app.get('/books/')
async def get_book_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return
