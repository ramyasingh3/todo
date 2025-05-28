import pytest
from todo_repository import TodoRepository

def test_create_todo():
    repo = TodoRepository()
    todo = repo.create("Test Todo", "Test Description")
    assert todo.id == 1
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert len(repo.get_all()) == 1

def test_get_by_id():
    repo = TodoRepository()
    todo = repo.create("Test Todo", "Test Description")
    found_todo = repo.get_by_id(1)
    assert found_todo == todo
    assert repo.get_by_id(999) is None

def test_get_all():
    repo = TodoRepository()
    todo1 = repo.create("Todo 1", "Description 1")
    todo2 = repo.create("Todo 2", "Description 2")
    todos = repo.get_all()
    assert len(todos) == 2
    assert todo1 in todos
    assert todo2 in todos

def test_update_todo():
    repo = TodoRepository()
    todo = repo.create("Test Todo", "Test Description")
    updated_todo = repo.update(1, "New Title", "New Description")
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Description"
    assert repo.update(999) is None

def test_delete_todo():
    repo = TodoRepository()
    todo = repo.create("Test Todo", "Test Description")
    assert repo.delete(1) is True
    assert len(repo.get_all()) == 0
    assert repo.delete(999) is False 