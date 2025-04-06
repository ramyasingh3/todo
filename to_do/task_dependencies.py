from datetime import datetime
from typing import Dict, List, Optional, Set
from collections import defaultdict

class DependentTask:
    def __init__(self, description: str, category: str, dependencies: Optional[List['DependentTask']] = None,
                 priority: int = 1, due_date: Optional[str] = None):
        self.description = description
        self.category = category
        self.dependencies = set(dependencies) if dependencies else set()
        self.dependents = set()  # Tasks that depend on this task
        self.priority = priority
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False
        self.completed_at = None

    def add_dependency(self, task: 'DependentTask') -> None:
        """Add a task that this task depends on."""
        self.dependencies.add(task)
        task.dependents.add(self)

    def remove_dependency(self, task: 'DependentTask') -> None:
        """Remove a dependency from this task."""
        self.dependencies.discard(task)
        task.dependents.discard(self)

    def can_complete(self) -> bool:
        """Check if all dependencies are completed."""
        return all(dep.completed for dep in self.dependencies)

    def complete_task(self) -> None:
        """Mark the task as completed if all dependencies are completed."""
        if self.can_complete():
            self.completed = True
            self.completed_at = datetime.now()
        else:
            incomplete_deps = [dep.description for dep in self.dependencies if not dep.completed]
            raise ValueError(f"Cannot complete task. Incomplete dependencies: {incomplete_deps}")

    def get_dependency_chain(self) -> List['DependentTask']:
        """Get all tasks in the dependency chain (including this task)."""
        chain = set()
        self._collect_dependency_chain(chain)
        return sorted(chain, key=lambda x: x.created_at)

    def _collect_dependency_chain(self, chain: Set['DependentTask']) -> None:
        """Helper method to collect all tasks in the dependency chain."""
        if self in chain:
            return
        chain.add(self)
        for dep in self.dependencies:
            dep._collect_dependency_chain(chain)

    def __str__(self) -> str:
        """String representation of the task."""
        status = "Completed" if self.completed else "Pending"
        deps_str = f", Dependencies: {', '.join(dep.description for dep in self.dependencies)}" if self.dependencies else ""
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        completed_at_str = f", Completed at: {self.completed_at}" if self.completed else ""
        return f"{self.description} (Category: {self.category}, Priority: {self.priority}{deps_str}{due_date_str}, Status: {status}{completed_at_str})"

class TaskDependencyManager:
    def __init__(self):
        self.categories: Dict[str, List[DependentTask]] = defaultdict(list)
        self.completed_tasks: List[DependentTask] = []
        self.all_tasks: Dict[str, DependentTask] = {}  # description -> task mapping

    def add_category(self, category_name: str) -> None:
        """Add a new category if it doesn't exist."""
        if category_name not in self.categories:
            self.categories[category_name] = []

    def add_task(self, description: str, category: str, dependencies: Optional[List[str]] = None,
                 priority: int = 1, due_date: Optional[str] = None) -> DependentTask:
        """Add a new task with dependencies to the specified category."""
        if category not in self.categories:
            self.add_category(category)
        
        # Create the task
        task = DependentTask(description, category, priority=priority, due_date=due_date)
        
        # Add dependencies if specified
        if dependencies:
            for dep_desc in dependencies:
                if dep_desc in self.all_tasks:
                    task.add_dependency(self.all_tasks[dep_desc])
                else:
                    raise ValueError(f"Dependency task '{dep_desc}' not found")
        
        # Add to collections
        self.categories[category].append(task)
        self.all_tasks[description] = task
        
        return task

    def get_ready_tasks(self) -> List[DependentTask]:
        """Get all tasks that can be completed (all dependencies are done)."""
        ready_tasks = []
        for tasks in self.categories.values():
            ready_tasks.extend([task for task in tasks if task.can_complete() and not task.completed])
        return sorted(ready_tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def get_blocked_tasks(self) -> List[DependentTask]:
        """Get all tasks that cannot be completed yet (some dependencies are not done)."""
        blocked_tasks = []
        for tasks in self.categories.values():
            blocked_tasks.extend([task for task in tasks if not task.can_complete() and not task.completed])
        return sorted(blocked_tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def get_tasks_by_category(self, category: str) -> List[DependentTask]:
        """Get all tasks in a specific category."""
        return self.categories.get(category, [])

    def get_all_tasks(self) -> List[DependentTask]:
        """Get all tasks across all categories."""
        all_tasks = []
        for category_tasks in self.categories.values():
            all_tasks.extend(category_tasks)
        return sorted(all_tasks, key=lambda x: (-x.priority, x.due_date or ""))

    def complete_task(self, task: DependentTask) -> None:
        """Mark a task as completed and move it to completed tasks."""
        if task in self.categories[task.category]:
            task.complete_task()
            self.categories[task.category].remove(task)
            self.completed_tasks.append(task)

    def get_completed_tasks(self) -> List[DependentTask]:
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
        
        # Print ready tasks
        ready_tasks = self.get_ready_tasks()
        if ready_tasks:
            result.append("\nReady Tasks:")
            for task in ready_tasks:
                result.append(f"  - {task}")
        
        # Print blocked tasks
        blocked_tasks = self.get_blocked_tasks()
        if blocked_tasks:
            result.append("\nBlocked Tasks:")
            for task in blocked_tasks:
                result.append(f"  - {task}")
        
        # Print completed tasks
        if self.completed_tasks:
            result.append("\nCompleted Tasks:")
            for task in self.completed_tasks:
                result.append(f"  - {task}")
        
        return "\n".join(result)

# Test cases
if __name__ == "__main__":
    # Create task manager
    manager = TaskDependencyManager()

    # Add some categories
    manager.add_category("Work")
    manager.add_category("Personal")

    # Add tasks with dependencies
    task1 = manager.add_task(
        "Write project proposal",
        "Work",
        priority=2,
        due_date="2024-04-10"
    )
    task2 = manager.add_task(
        "Review proposal",
        "Work",
        dependencies=["Write project proposal"],
        priority=2,
        due_date="2024-04-12"
    )
    task3 = manager.add_task(
        "Implement feature",
        "Work",
        dependencies=["Review proposal"],
        priority=3,
        due_date="2024-04-15"
    )
    task4 = manager.add_task(
        "Test feature",
        "Work",
        dependencies=["Implement feature"],
        priority=2,
        due_date="2024-04-17"
    )
    task5 = manager.add_task(
        "Call mom",
        "Personal",
        priority=3
    )

    # Print all tasks
    print("Initial state:")
    print(manager)
    print()

    # Complete tasks in order
    try:
        manager.complete_task(task1)
        print("After completing 'Write project proposal':")
        print(manager)
        print()

        manager.complete_task(task2)
        print("After completing 'Review proposal':")
        print(manager)
        print()

        manager.complete_task(task3)
        print("After completing 'Implement feature':")
        print(manager)
        print()

        manager.complete_task(task4)
        print("After completing 'Test feature':")
        print(manager)
        print()

        # Try to complete a task with incomplete dependencies
        try:
            manager.complete_task(task3)  # Already completed
            print("After completing 'Implement feature' again:")
            print(manager)
        except ValueError as e:
            print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}") 