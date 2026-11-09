# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for managing books with FastAPI. Practice defining HTTP routes, handling path parameters, validating request data with Pydantic, and returning appropriate status codes.

## 📝 Tasks

### 🛠️ Task 1: Create Read Routes

#### Description
Use the provided `main.py` scaffold to add routes for listing all books and retrieving one book by its ID. Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, then run the API with `uvicorn main:app --reload`.

#### Requirements
Completed program should:

- Return the books as JSON from `GET /books`
- Return one book from `GET /books/{book_id}` when its ID exists
- Return HTTP 404 when the requested book ID does not exist
- Keep book data in the provided in-memory collection

### 🛠️ Task 2: Add a Create Route

#### Description
Add an endpoint that accepts a new book, validates its data, and adds it to the in-memory collection. Use FastAPI's interactive documentation at `/docs` to try the endpoints.

#### Requirements
Completed program should:

- Accept a book's `title`, `author`, and integer `year` in a `POST /books` request
- Use the provided Pydantic model to validate the request body
- Assign the new book a unique ID and include that ID in the response
- Return HTTP 201 when a book is created and HTTP 422 for invalid request data
- Verify listing, retrieving, creating, missing IDs, and invalid request data through `/docs`