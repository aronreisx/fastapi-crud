from fastapi import FastAPI
from dataclasses import dataclass
from typing import List, Dict

app = FastAPI()

@dataclass
class Book:
    id: int
    title: str
    author: str

@app.get('/', tags=['ROOT'])
async def root() -> Dict[str, str]:
    return{'app': 'works'}

@app.get('/books', tags=['books'])
async def get_books() -> Dict[str, List[Book]]:
    return {'data': books}

@app.post('/books', tags=['books'], status_code=201)
async def add_book(book: Book) -> Dict[str, List[Book]]:
    books.append(book)
    return {'data': books}

@app.put('/books/{id}', tags=['books'], status_code=202)
async def update_book(id: int, newBookInfo: Book) -> Dict[str, Book or str]:
    for book in books:
        if int(book['id']) == id:
            book = newBookInfo
            return {'data': book}
    return {'data': f'The book with {id} was not found'}

@app.delete('/books/{id}', tags=['books'], status_code=202)
async def delete_book(id: int) -> Dict[str, str]:
    for book in books:
        if int(book['id']) == id:
            books.remove(book)
            return {'data': f'The book with {id} was deleted'}
    return {'data': f'The book with {id} was not found'}

books: List[Book] = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1'
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2'
    }
]
