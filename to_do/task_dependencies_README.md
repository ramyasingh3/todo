# Task Dependencies

## Overview
A task management system that supports task dependencies, allowing users to specify which tasks must be completed before others can start. This is particularly useful for managing complex projects with sequential or parallel tasks.

## Features
1. **Dependency Management**:
   - Add dependencies between tasks
   - Remove dependencies
   - Check if a task can be completed
   - Get dependency chain for a task
   - Track both dependencies and dependents

2. **Task Properties**:
   - Description
   - Category
   - Dependencies
   - Priority level
   - Optional due date
   - Creation timestamp
   - Completion status
   - Completion timestamp

3. **Core Operations**:
   - Add tasks with dependencies
   - Get ready tasks (all dependencies completed)
   - Get blocked tasks (some dependencies incomplete)
   - Complete tasks (only if dependencies are done)
   - View completed tasks
   - Clear completed tasks
   - Get all categories

## Usage

### Basic Usage
```python
from task_dependencies import TaskDependencyManager

# Create task manager
manager = TaskDependencyManager()

# Add tasks with dependencies
task1 = manager.add_task(
    "Write project proposal",
    "Work",
    priority=2
)
task2 = manager.add_task(
    "Review proposal",
    "Work",
    dependencies=["Write project proposal"],
    priority=2
)

# Get ready tasks
ready_tasks = manager.get_ready_tasks()
for task in ready_tasks:
    print(task)
```

### Advanced Usage
```python
# Add complex dependency chain
task1 = manager.add_task("Design", "Work", priority=2)
task2 = manager.add_task("Implement", "Work", dependencies=["Design"], priority=3)
task3 = manager.add_task("Test", "Work", dependencies=["Implement"], priority=2)
task4 = manager.add_task("Deploy", "Work", dependencies=["Test"], priority=1)

# Get blocked tasks
blocked_tasks = manager.get_blocked_tasks()
for task in blocked_tasks:
    print(task)

# Complete tasks in order
manager.complete_task(task1)  # Design
manager.complete_task(task2)  # Implement
manager.complete_task(task3)  # Test
manager.complete_task(task4)  # Deploy
```

## Implementation Details

### DependentTask Class
- `__init__`: Initialize task with description, category, dependencies, priority, and optional due date
- `add_dependency`: Add a task that this task depends on
- `remove_dependency`: Remove a dependency from this task
- `can_complete`: Check if all dependencies are completed
- `complete_task`: Mark task as completed if dependencies are done
- `get_dependency_chain`: Get all tasks in the dependency chain
- `__str__`: String representation of the task

### TaskDependencyManager Class
- `add_category`: Add new category
- `add_task`: Add task with dependencies to category
- `get_ready_tasks`: Get tasks that can be completed
- `get_blocked_tasks`: Get tasks that cannot be completed yet
- `get_tasks_by_category`: Get tasks in specific category
- `get_all_tasks`: Get all tasks sorted by priority and due date
- `complete_task`: Mark task as completed
- `get_completed_tasks`: Get all completed tasks
- `clear_completed_tasks`: Remove all completed tasks
- `get_categories`: Get all category names
- `__str__`: String representation of the task manager

## Time Complexity
- Add task: O(1)
- Add dependency: O(1)
- Get ready tasks: O(N) where N is total number of tasks
- Get blocked tasks: O(N) where N is total number of tasks
- Complete task: O(1)
- Get dependency chain: O(N) where N is number of tasks in chain
- Get completed tasks: O(1)
- Clear completed tasks: O(1)
- Get categories: O(1)

## Space Complexity
- O(N + M + D) where N is total tasks, M is categories, and D is dependencies

## Example Output
```
Ready Tasks:
  - Write project proposal (Category: Work, Priority: 2, Due: 2024-04-10, Status: Pending)
  - Call mom (Category: Personal, Priority: 3, Status: Pending)

Blocked Tasks:
  - Review proposal (Category: Work, Priority: 2, Dependencies: Write project proposal, Due: 2024-04-12, Status: Pending)
  - Implement feature (Category: Work, Priority: 3, Dependencies: Review proposal, Due: 2024-04-15, Status: Pending)
  - Test feature (Category: Work, Priority: 2, Dependencies: Implement feature, Due: 2024-04-17, Status: Pending)

Completed Tasks:
  - Write project proposal (Category: Work, Priority: 2, Due: 2024-04-10, Status: Completed, Completed at: 2024-04-06 15:30:00)
```

## Common Applications
- Project management with sequential tasks
- Software development workflows
- Event planning with dependencies
- Study planning with prerequisites
- Workflow management
- Process automation 