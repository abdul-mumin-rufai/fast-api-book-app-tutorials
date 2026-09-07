from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'name': 'Abdul-Mumin', 'author': 'Author One', 'category': 'Computing'},
    {'name': 'Abdul-Mumin', 'author': 'Author One', 'category': 'Computing'},
    {'name': 'Rufai-Bawa', 'author': 'Author One', 'category': 'Economics'},
    {'name': 'Rukayatu-Yakubu', 'author': 'Author One', 'category': 'Geography'},
    {'name': 'Bintu-Bawa', 'author': 'Author One', 'category': 'Calculus'},
    {'name': 'Abdul-Mumin', 'author': 'Author One', 'category': 'Economics'},
    {'name': 'Tijani-Yakubu', 'author': 'Author One', 'category': 'Maths'},
    {'name': 'Fatawu-Yakubu', 'author': 'Author One', 'category': 'English'},

]


@app.get('/books')
async def my_first_end_point():
    return BOOKS
