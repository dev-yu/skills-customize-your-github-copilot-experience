from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    2: {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
}

# Task 1: Add GET routes to list books and retrieve a book by ID.
# Task 2: Add a POST route to create a book using the BookCreate model.