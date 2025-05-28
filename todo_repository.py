from typing import List, Optional
from todo_model import Todo

class TodoRepository:
    def __init__(self):
        self.todos: List[Todo] = []
        self.next_id = 1

    def create(self, title: str, description: str) -> Todo:
        todo = Todo(self.next_id, title, description)
        self.next_id += 1
        self.todos.append(todo)
        return todo

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def get_all(self) -> List[Todo]:
        return self.todos

    def update(self, todo_id: int, title: str = None, description: str = None) -> Optional[Todo]:
        todo = self.get_by_id(todo_id)
        if todo:
            if title:
                todo.update_title(title)
            if description:
                todo.update_description(description)
        return todo

    def delete(self, todo_id: int) -> bool:
        todo = self.get_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            return True
        return False 