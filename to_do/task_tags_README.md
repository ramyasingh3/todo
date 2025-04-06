# Task Tags

## Overview
A task management system that extends the category-based organization by adding tags to tasks. This allows for more flexible and granular organization of tasks, enabling users to filter and group tasks in multiple ways.

## Features
1. **Tag Management**:
   - Add multiple tags to tasks
   - Remove tags from tasks
   - Check if a task has a specific tag
   - Get all unique tags used in tasks

2. **Task Properties**:
   - Description
   - Category
   - Multiple tags
   - Priority level
   - Optional due date
   - Creation timestamp
   - Completion status
   - Completion timestamp

3. **Core Operations**:
   - Add tasks with tags
   - Get tasks by single tag
   - Get tasks by multiple tags
   - Get all tasks across categories
   - Mark tasks as completed
   - View completed tasks
   - Clear completed tasks
   - Get all categories

## Usage

### Basic Usage
```python
from task_tags import TaggedTaskManager

# Create task manager
manager = TaggedTaskManager()

# Add tasks with tags
task = manager.add_task(
    "Complete project",
    "Work",
    tags=["urgent", "documentation"],
    priority=2
)

# Get tasks by tag
urgent_tasks = manager.get_tasks_by_tag("urgent")
for task in urgent_tasks:
    print(task)
```

### Advanced Usage
```python
# Add task with multiple tags
task = manager.add_task(
    "Submit report",
    "Work",
    tags=["urgent", "documentation", "weekly"],
    priority=2,
    due_date="2024-04-15"
)

# Get tasks by multiple tags
tasks = manager.get_tasks_by_tags(["urgent", "documentation"])
for task in tasks:
    print(task)

# Get all tags
all_tags = manager.get_all_tags()
print("Available tags:", all_tags)
```

## Implementation Details

### TaggedTask Class
- `__init__`: Initialize task with description, category, tags, priority, and optional due date
- `add_tag`: Add a new tag to the task
- `remove_tag`: Remove a tag from the task
- `has_tag`: Check if the task has a specific tag
- `complete_task`: Mark task as completed
- `__str__`: String representation of the task

### TaggedTaskManager Class
- `add_category`: Add new category
- `add_task`: Add task with tags to category
- `get_tasks_by_tag`: Get tasks with specific tag
- `get_tasks_by_tags`: Get tasks with all specified tags
- `get_tasks_by_category`: Get tasks in specific category
- `get_all_tasks`: Get all tasks sorted by priority and due date
- `get_all_tags`: Get all unique tags
- `complete_task`: Mark task as completed
- `get_completed_tasks`: Get all completed tasks
- `clear_completed_tasks`: Remove all completed tasks
- `get_categories`: Get all category names
- `__str__`: String representation of the task manager

## Time Complexity
- Add task: O(1)
- Get tasks by tag: O(N) where N is total number of tasks
- Get tasks by multiple tags: O(N * M) where N is total tasks and M is number of tags
- Get all tags: O(1)
- Complete task: O(N) where N is number of tasks in category
- Get completed tasks: O(1)
- Clear completed tasks: O(1)
- Get categories: O(1)

## Space Complexity
- O(N + M + T) where N is total tasks, M is categories, and T is unique tags

## Example Output
```
Category: Work
  - Fix critical bug (Category: Work, Priority: 3, Tags: urgent, bug, Due: 2024-04-08, Status: Pending)
  - Complete project documentation (Category: Work, Priority: 2, Tags: urgent, documentation, Due: 2024-04-10, Status: Pending)
  - Update resume (Category: Work, Priority: 2, Tags: career, Status: Pending)

Category: Personal
  - Call mom (Category: Personal, Priority: 3, Tags: family, weekly, Status: Pending)

Category: Shopping
  - Buy groceries (Category: Shopping, Priority: 1, Tags: food, weekly, Due: 2024-04-08, Status: Completed, Completed at: 2024-04-06 15:30:00)
```

## Common Applications
- Project management with multiple attributes
- Task filtering and organization
- Work tracking with multiple dimensions
- Study planning with different subjects
- Event planning with various aspects
- Personal organization with multiple contexts 