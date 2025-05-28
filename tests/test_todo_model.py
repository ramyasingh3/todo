import pytest
from todo_model import Todo

def test_todo_creation():
    todo = Todo(1, "Test Todo", "Test Description")
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed == False

def test_todo_mark_completed():
    todo = Todo(1, "Test Todo", "Test Description")
    todo.mark_completed()
    assert todo.completed == True

def test_todo_mark_incomplete():
    todo = Todo(1, "Test Todo", "Test Description")
    todo.mark_completed()
    todo.mark_incomplete()
    assert todo.completed == False

def test_todo_update_title():
    todo = Todo(1, "Test Todo", "Test Description")
    todo.update_title("New Title")
    assert todo.title == "New Title"

def test_todo_update_description():
    todo = Todo(1, "Test Todo", "Test Description")
    todo.update_description("New Description")
    assert todo.description == "New Description" 