# ==========================================
# CHAPTER 7: FASTAPI BASICS (TODO APP)
# ==========================================


# ==========================================
# 1) INTRODUCTION TO FASTAPI
# ==========================================

"""
Definition:
FastAPI is a modern Python web framework used to build APIs quickly.

Features:
- Fast performance
- Easy to use
- Automatic documentation (/docs)
- Uses Python type hints
"""


# ==========================================
# 2) SETUP (WINDOWS / LINUX / MAC)
# ==========================================

"""
Step 1: Create project folder
> mkdir fastapi-todo
> cd fastapi-todo

Step 2: Create virtual environment

Windows:
> python -m venv venv
> venv\Scripts\activate

Linux/Mac:
> python3 -m venv venv
> source venv/bin/activate

Step 3: Install dependencies
> pip install fastapi uvicorn

Step 4: Create file
> main.py
"""


# ==========================================
# 3) FIRST FASTAPI APP
# ==========================================

"""
Run server:
> uvicorn main:app --reload
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


"""
Open:
http://127.0.0.1:8000

Docs:
http://127.0.0.1:8000/docs
"""


# ==========================================
# 4) TODO APP (IN-MEMORY)
# ==========================================

todos = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn FastAPI", "completed": False},
]


# Model for creating todo
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# Model for updating todo (BEST PRACTICE)
class TodoUpdate(BaseModel):
    title: str
    completed: bool


# ------------------------------------------
# 4.1 GET ALL TODOS
# ------------------------------------------

@app.get("/todos")
def get_todos():
    return todos


# ------------------------------------------
# 4.2 GET TODO BY ID
# ------------------------------------------

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}


# ------------------------------------------
# 4.3 CREATE TODO
# ------------------------------------------

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo.dict())
    return {"message": "Created", "todo": todo}


# ------------------------------------------
# 4.4 UPDATE TODO (TWO OPTIONS)
# ------------------------------------------

"""
OPTION 1 (BEGINNER)  NOT RECOMMENDED
- ID in URL + body
- Risk of mismatch
"""


@app.put("/v1/todos/{todo_id}")
def update_todo_v1(todo_id: int, updated: Todo):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i] = updated.dict()
            return {"message": "Updated (v1)"}
    return {"error": "Todo not found"}


"""
Example:
PUT /v1/todos/1

{
  "id": 1,
  "title": "Updated Task",
  "completed": true
}
"""


"""
OPTION 2 (BEST PRACTICE) 
- ID only in URL
- Body contains only updated data
"""


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoUpdate):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[i]["title"] = updated.title
            todos[i]["completed"] = updated.completed
            return {"message": "Updated"}
    return {"error": "Todo not found"}


"""
Example:
PUT /todos/1

{
  "title": "Updated Task",
  "completed": true
}
"""


# ------------------------------------------
# 4.5 DELETE TODO
# ------------------------------------------

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            return {"message": "Deleted"}
    return {"error": "Todo not found"}


# ==========================================
# 5) TESTING USING POSTMAN
# ==========================================

"""
Tool: Postman (API testing)

Base URL:
http://127.0.0.1:8000
"""


# ------------------------------------------
# 5.1 GET ALL
# ------------------------------------------

"""
GET /todos
"""


# ------------------------------------------
# 5.2 GET BY ID
# ------------------------------------------

"""
GET /todos/1
"""


# ------------------------------------------
# 5.3 CREATE
# ------------------------------------------

"""
POST /todos

Body (JSON):
{
  "id": 3,
  "title": "Build API",
  "completed": false
}
"""


# ------------------------------------------
# 5.4 UPDATE
# ------------------------------------------

"""
PUT /todos/1

Body:
{
  "title": "Updated Task",
  "completed": true
}
"""


# ------------------------------------------
# 5.5 DELETE
# ------------------------------------------

"""
DELETE /todos/1
"""


# ==========================================
# 6) SUMMARY
# ==========================================

"""
FastAPI:
- FastAPI()
- @app.get()
- @app.post()
- @app.put()
- @app.delete()

Setup:
- venv
- install fastapi, uvicorn
- run server

Testing:
- Swagger → /docs
- Postman

Todo Endpoints:
✔ GET /todos
✔ GET /todos/{id}
✔ POST /todos
✔ PUT /todos/{id}
✔ DELETE /todos/{id}


"""
