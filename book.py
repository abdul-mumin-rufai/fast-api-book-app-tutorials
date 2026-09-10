from fastapi import FastAPI, Body

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


@app.get('/books/{author_name}/')
async def get_book_by_query_and_author(author_name: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


# THe POST HTTPS METHOD
@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


# THE PUT REQUEST METHOD
@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for index in range(len(BOOKS)):
        if BOOKS[index].get('name').casefold() == updated_book.get('name').casefold():
            BOOKS[index] = updated_book

