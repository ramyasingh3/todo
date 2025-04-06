from datetime import datetime
from typing import Dict, List, Optional

class Task:
    def __init__(self, description: str, category: str, priority: int = 1, due_date: Optional[str] = None):
        self.description = description
        self.category = category
        self.priority = priority
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None

    def complete_task(self):
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        completed_at_str = f", Completed at: {self.completed_at}" if self.completed else ""
        return f"{self.description} (Category: {self.category}, Priority: {self.priority}{due_date_str}, Status: {status}{completed_at_str})"

class TaskManager:
    def __init__(self):
        self.categories: Dict[str, List[Task]] = {}
        self.completed_tasks: List[Task] = []

    def add_category(self, category_name: str) -> None:
        """Add a new category if it doesn't exist."""
        if category_name not in self.categories:
            self.categories[category_name] = []

    def add_task(self, description: str, category: str, priority: int = 1, due_date: Optional[str] = None) -> Task:
        """Add a new task to the specified category."""
        if category not in self.categories:
            self.add_category(category)
        
        task = Task(description, category, priority, due_date)
        self.categories[category].append(task)
        return task

    def get_tasks_by_category(self, category: str) -> List[Task]:
        """Get all tasks in a specific category."""
        return self.categories.get(category, [])

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks across all categories."""
        all_tasks = []
        for category_tasks in self.categories.values():
            all_tasks.extend(category_tasks)
        return sorted(all_tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def complete_task(self, task: Task) -> None:
        """Mark a task as completed and move it to completed tasks."""
        if task in self.categories[task.category]:
            task.complete_task()
            self.categories[task.category].remove(task)
            self.completed_tasks.append(task)

    def get_completed_tasks(self) -> List[Task]:
        """Get all completed tasks."""
        return self.completed_tasks

    def clear_completed_tasks(self) -> None:
        """Remove all completed tasks."""
        self.completed_tasks.clear()

    def get_categories(self) -> List[str]:
        """Get all category names."""
        return list(self.categories.keys())

    def __str__(self) -> str:
        """String representation of the task manager."""
        result = []
        for category, tasks in self.categories.items():
            result.append(f"\nCategory: {category}")
            for task in sorted(tasks, key=lambda x: (-x.priority, x.due_date or "")):
                result.append(f"  - {task}")
        
        if self.completed_tasks:
            result.append("\nCompleted Tasks:")
            for task in self.completed_tasks:
                result.append(f"  - {task}")
        
        return "\n".join(result)

# Test cases
if __name__ == "__main__":
    # Create task manager
    manager = TaskManager()

    # Add some categories
    manager.add_category("Work")
    manager.add_category("Personal")
    manager.add_category("Shopping")

    # Add tasks to different categories
    task1 = manager.add_task("Complete project documentation", "Work", priority=2, due_date="2024-04-10")
    task2 = manager.add_task("Buy groceries", "Shopping", priority=1, due_date="2024-04-08")
    task3 = manager.add_task("Call mom", "Personal", priority=3)
    task4 = manager.add_task("Fix critical bug", "Work", priority=3, due_date="2024-04-08")
    task5 = manager.add_task("Update resume", "Work", priority=2)

    # Print all tasks
    print("All tasks:")
    print(manager)
    print()

    # Complete some tasks
    manager.complete_task(task2)
    manager.complete_task(task4)

    # Print tasks after completion
    print("Tasks after completion:")
    print(manager)
    print()

    # Get tasks by category
    print("Work tasks:")
    for task in manager.get_tasks_by_category("Work"):
        print(f"  - {task}")
    print()

    # Get all categories
    print("Categories:", manager.get_categories())
    print()

    # Clear completed tasks
    manager.clear_completed_tasks()
    print("After clearing completed tasks:")
    print(manager) 