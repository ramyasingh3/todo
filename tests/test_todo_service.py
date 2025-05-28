import pytest
from todo_service import TodoService

def test_create_todo():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    assert todo.title == "Test Todo"
    assert todo.description == "Test Description"
    assert todo.completed == False

def test_create_todo_empty_title():
    service = TodoService()
    with pytest.raises(ValueError):
        service.create_todo("", "Test Description")

def test_get_todo():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    found_todo = service.get_todo(1)
    assert found_todo == todo
    assert service.get_todo(999) is None

def test_get_all_todos():
    service = TodoService()
    todo1 = service.create_todo("Todo 1", "Description 1")
    todo2 = service.create_todo("Todo 2", "Description 2")
    todos = service.get_all_todos()
    assert len(todos) == 2
    assert todo1 in todos
    assert todo2 in todos

def test_update_todo():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    updated_todo = service.update_todo(1, "New Title", "New Description")
    assert updated_todo.title == "New Title"
    assert updated_todo.description == "New Description"
    assert service.update_todo(999) is None

def test_update_todo_empty_title():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    with pytest.raises(ValueError):
        service.update_todo(1, "", "New Description")

def test_delete_todo():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    assert service.delete_todo(1) is True
    assert len(service.get_all_todos()) == 0
    assert service.delete_todo(999) is False

def test_mark_todo_completed():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    updated_todo = service.mark_todo_completed(1)
    assert updated_todo.completed is True
    assert service.mark_todo_completed(999) is None

def test_mark_todo_incomplete():
    service = TodoService()
    todo = service.create_todo("Test Todo", "Test Description")
    service.mark_todo_completed(1)
    updated_todo = service.mark_todo_incomplete(1)
    assert updated_todo.completed is False
    assert service.mark_todo_incomplete(999) is None 