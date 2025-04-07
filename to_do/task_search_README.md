# Task Search

## Feature Description
The Task Search feature provides comprehensive search capabilities for tasks in the to-do list system. It allows users to search for tasks based on various criteria including name, description, priority, due date, tags, and completion status. The feature supports both simple and advanced search operations.

## Search Methods

### 1. Name Search
- Case-sensitive or case-insensitive substring matching
- Returns tasks whose names contain the search query
- Example: `search_by_name("project")`

### 2. Description Search
- Case-sensitive or case-insensitive substring matching
- Returns tasks whose descriptions contain the search query
- Example: `search_by_description("Friday")`

### 3. Priority Search
- Exact matching of priority levels
- Returns tasks with the specified priority
- Example: `search_by_priority(2)`

### 4. Due Date Search
- Range-based search using start and end dates
- Returns tasks due within the specified date range
- Example: `search_by_due_date("2024-03-10", "2024-03-15")`

### 5. Tag Search
- Supports matching all or any tags
- Returns tasks that have the specified tags
- Example: `search_by_tags(["work", "urgent"], match_all=True)`

### 6. Status Search
- Search by completion status
- Returns tasks that are either completed or not completed
- Example: `search_by_status(completed=True)`

### 7. Advanced Search
- Combines multiple search criteria
- Returns tasks that match all specified conditions
- Example: `advanced_search(name="project", priority=2, tags=["work"])`

## Usage Examples

### Basic Usage
```python
from task_search import Task, TaskSearch

# Create some tasks
tasks = [
    Task("Complete project", "Finish by Friday", 2, "2024-03-15", ["work", "urgent"]),
    Task("Buy groceries", "Milk, eggs", 3, "2024-03-10", ["shopping"])
]

# Initialize search
search = TaskSearch(tasks)

# Search by name
results = search.search_by_name("project")
for task in results:
    print(task)
```

### Advanced Search
```python
# Search using multiple criteria
results = search.advanced_search(
    name="project",
    priority=2,
    tags=["work"],
    match_all_tags=True
)
for task in results:
    print(task)
```

## Implementation Details

### Task Class
- Represents a single task with properties:
  - name
  - description
  - priority
  - due_date
  - tags
  - completed
  - created_at

### TaskSearch Class
- Central class for all search operations
- Methods for individual search criteria
- Advanced search combining multiple criteria
- Type hints for better code clarity

## Performance Considerations
- All search methods use list comprehensions for efficient filtering
- Case-insensitive search uses string lowercasing
- Date range search includes error handling for invalid dates
- Tag search supports both AND and OR operations

## Common Applications
- Task filtering and organization
- Finding specific tasks quickly
- Generating reports based on task properties
- Task management and prioritization
- Data analysis and visualization 