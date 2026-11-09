# 📘 Assignment: Testing FastAPI Routes with unittest

## 🎯 Objective

Write automated tests for the book API from the FastAPI assignment using Python's built-in `unittest` framework. Check route responses, request validation, and error handling without adding a separate test framework.

## 📝 Tasks

### 🛠️ Task 1: Test the Read Routes

#### Description
Continue from the completed FastAPI book API assignment. Place the provided `test_main.py` beside your `main.py`, install the `httpx` package with `python -m pip install httpx`, and run the tests with `python -m unittest -v`.

#### Requirements
Completed test suite should:

- Use `unittest.TestCase` and FastAPI's `TestClient`
- Keep the provided test that verifies `GET /books` returns HTTP 200 and a JSON list
- Add a test that verifies `GET /books/{book_id}` returns the requested book and HTTP 200
- Add a test that verifies an unknown book ID returns HTTP 404
- Report test results when run with `python -m unittest -v`

### 🛠️ Task 2: Test Creating and Validating Books

#### Description
Extend the test suite to cover creating a book and sending invalid request data to the API.

#### Requirements
Completed test suite should:

- Verify a valid `POST /books` request returns HTTP 201
- Verify the response includes the submitted title, author, and year, plus a unique ID
- Verify a request with an invalid year returns HTTP 422
- Run all read-route and create-route tests together successfully