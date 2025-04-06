from datetime import datetime
from typing import Dict, List, Optional, Set

class TaggedTask:
    def __init__(self, description: str, category: str, tags: Optional[List[str]] = None, 
                 priority: int = 1, due_date: Optional[str] = None):
        self.description = description
        self.category = category
        self.tags = set(tags) if tags else set()
        self.priority = priority
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None

    def add_tag(self, tag: str) -> None:
        """Add a new tag to the task."""
        self.tags.add(tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the task."""
        self.tags.discard(tag)

    def has_tag(self, tag: str) -> bool:
        """Check if the task has a specific tag."""
        return tag in self.tags

    def complete_task(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        self.completed_at = datetime.now()

    def __str__(self) -> str:
        """String representation of the task."""
        status = "Completed" if self.completed else "Pending"
        tags_str = f", Tags: {', '.join(sorted(self.tags))}" if self.tags else ""
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        completed_at_str = f", Completed at: {self.completed_at}" if self.completed else ""
        return f"{self.description} (Category: {self.category}, Priority: {self.priority}{tags_str}{due_date_str}, Status: {status}{completed_at_str})"

class TaggedTaskManager:
    def __init__(self):
        self.categories: Dict[str, List[TaggedTask]] = {}
        self.completed_tasks: List[TaggedTask] = []
        self.all_tags: Set[str] = set()

    def add_category(self, category_name: str) -> None:
        """Add a new category if it doesn't exist."""
        if category_name not in self.categories:
            self.categories[category_name] = []

    def add_task(self, description: str, category: str, tags: Optional[List[str]] = None,
                 priority: int = 1, due_date: Optional[str] = None) -> TaggedTask:
        """Add a new task with tags to the specified category."""
        if category not in self.categories:
            self.add_category(category)
        
        task = TaggedTask(description, category, tags, priority, due_date)
        self.categories[category].append(task)
        
        # Update all tags set
        if tags:
            self.all_tags.update(tags)
            
        return task

    def get_tasks_by_tag(self, tag: str) -> List[TaggedTask]:
        """Get all tasks with a specific tag."""
        tasks = []
        for category_tasks in self.categories.values():
            tasks.extend([task for task in category_tasks if task.has_tag(tag)])
        return sorted(tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def get_tasks_by_tags(self, tags: List[str]) -> List[TaggedTask]:
        """Get all tasks that have all the specified tags."""
        tasks = []
        for category_tasks in self.categories.values():
            tasks.extend([task for task in category_tasks if all(task.has_tag(tag) for tag in tags)])
        return sorted(tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def get_tasks_by_category(self, category: str) -> List[TaggedTask]:
        """Get all tasks in a specific category."""
        return self.categories.get(category, [])

    def get_all_tasks(self) -> List[TaggedTask]:
        """Get all tasks across all categories."""
        all_tasks = []
        for category_tasks in self.categories.values():
            all_tasks.extend(category_tasks)
        return sorted(all_tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def get_all_tags(self) -> List[str]:
        """Get all unique tags used in tasks."""
        return sorted(self.all_tags)

    def complete_task(self, task: TaggedTask) -> None:
        """Mark a task as completed and move it to completed tasks."""
        if task in self.categories[task.category]:
            task.complete_task()
            self.categories[task.category].remove(task)
            self.completed_tasks.append(task)

    def get_completed_tasks(self) -> List[TaggedTask]:
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
    manager = TaggedTaskManager()

    # Add some categories
    manager.add_category("Work")
    manager.add_category("Personal")
    manager.add_category("Shopping")

    # Add tasks with tags
    task1 = manager.add_task(
        "Complete project documentation",
        "Work",
        tags=["urgent", "documentation"],
        priority=2,
        due_date="2024-04-10"
    )
    task2 = manager.add_task(
        "Buy groceries",
        "Shopping",
        tags=["food", "weekly"],
        priority=1,
        due_date="2024-04-08"
    )
    task3 = manager.add_task(
        "Call mom",
        "Personal",
        tags=["family", "weekly"],
        priority=3
    )
    task4 = manager.add_task(
        "Fix critical bug",
        "Work",
        tags=["urgent", "bug"],
        priority=3,
        due_date="2024-04-08"
    )
    task5 = manager.add_task(
        "Update resume",
        "Work",
        tags=["career"],
        priority=2
    )

    # Print all tasks
    print("All tasks:")
    print(manager)
    print()

    # Get tasks by tag
    print("Tasks with tag 'urgent':")
    for task in manager.get_tasks_by_tag("urgent"):
        print(f"  - {task}")
    print()

    # Get tasks by multiple tags
    print("Tasks with tags 'weekly' and 'food':")
    for task in manager.get_tasks_by_tags(["weekly", "food"]):
        print(f"  - {task}")
    print()

    # Get all tags
    print("All tags:", manager.get_all_tags())
    print()

    # Complete some tasks
    manager.complete_task(task2)
    manager.complete_task(task4)

    # Print tasks after completion
    print("Tasks after completion:")
    print(manager)
    print()

    # Clear completed tasks
    manager.clear_completed_tasks()
    print("After clearing completed tasks:")
    print(manager) 