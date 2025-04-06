# Task Priority Queue

## Overview
A priority queue implementation for managing tasks with different priority levels and due dates. This implementation uses Python's `heapq` module to efficiently manage task priorities and provides a clean interface for task management.

## Features
1. **Priority-based Task Management**:
   - Tasks are ordered by priority (higher numbers = higher priority)
   - For tasks with same priority, earlier due dates come first
   - Tasks without due dates are ordered by creation time

2. **Task Properties**:
   - Description
   - Priority level
   - Optional due date
   - Creation timestamp
   - Completion status
   - Completion timestamp

3. **Core Operations**:
   - Add new tasks
   - Get next highest priority task
   - Mark tasks as completed
   - View all tasks in priority order
   - View completed tasks
   - Clear completed tasks

## Usage

### Basic Usage
```python
from priority_queue import TaskPriorityQueue

# Create a task queue
task_queue = TaskPriorityQueue()

# Add tasks with different priorities
task1 = task_queue.add_task("Complete project documentation", priority=2)
task2 = task_queue.add_task("Fix critical bug", priority=3)
task3 = task_queue.add_task("Update documentation", priority=1)

# Get next task to work on
next_task = task_queue.get_next_task()
print(f"Next task: {next_task.description}")

# Mark a task as completed
task_queue.complete_task(task2)
```

### Advanced Usage
```python
# Add task with due date
task = task_queue.add_task(
    "Submit report",
    priority=2,
    due_date="2024-04-15"
)

# Get all tasks in priority order
all_tasks = task_queue.get_all_tasks()
for task in all_tasks:
    print(f"{task.description} (Priority: {task.priority})")

# Get completed tasks
completed = task_queue.get_completed_tasks()
for task in completed:
    print(f"{task.description} (Completed at: {task.completed_at})")
```

## Implementation Details

### Task Class
- `__init__`: Initialize task with description, priority, and optional due date
- `__lt__`: Custom comparison for priority queue ordering
- Properties: description, priority, due_date, created_at, completed, completed_at

### TaskPriorityQueue Class
- `add_task`: Add new task to the queue
- `get_next_task`: Get and remove highest priority task
- `complete_task`: Mark task as completed
- `get_all_tasks`: Get all tasks in priority order
- `get_completed_tasks`: Get all completed tasks
- `clear_completed_tasks`: Remove all completed tasks
- `__str__`: String representation of the queue

## Time Complexity
- Add task: O(log N)
- Get next task: O(log N)
- Complete task: O(1)
- Get all tasks: O(N log N)
- Get completed tasks: O(1)
- Clear completed tasks: O(1)

## Space Complexity
- O(N) where N is the number of tasks

## Example Output
```
Current Tasks:
- Fix critical bug (Priority: 3, Due: 2024-04-08, Status: Pending)
- Complete project documentation (Priority: 2, Due: 2024-04-10, Status: Pending)
- Review pull requests (Priority: 1, Status: Pending)
- Update dependencies (Priority: 1, Due: 2024-04-15, Status: Pending)

Completed Tasks:
- Fix critical bug (Completed at: 2024-04-06 15:30:00)
- Review pull requests (Completed at: 2024-04-06 15:35:00)
```

## Common Use Cases
- Project management
- Task scheduling
- To-do list applications
- Work queue management
- Priority-based task tracking 