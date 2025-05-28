from typing import List, Optional
from todo_model import Todo
from todo_repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repository = TodoRepository()

    def create_todo(self, title: str, description: str) -> Todo:
        if not title:
            raise ValueError("Title cannot be empty")
        return self.repository.create(title, description)

    def get_todo(self, todo_id: int) -> Optional[Todo]:
        return self.repository.get_by_id(todo_id)

    def get_all_todos(self) -> List[Todo]:
        return self.repository.get_all()

    def update_todo(self, todo_id: int, title: str = None, description: str = None) -> Optional[Todo]:
        if title == "":
            raise ValueError("Title cannot be empty")
        return self.repository.update(todo_id, title, description)

    def delete_todo(self, todo_id: int) -> bool:
        return self.repository.delete(todo_id)

    def mark_todo_completed(self, todo_id: int) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo:
            todo.mark_completed()
        return todo

    def mark_todo_incomplete(self, todo_id: int) -> Optional[Todo]:
        todo = self.get_todo(todo_id)
        if todo:
            todo.mark_incomplete()
        return todo 