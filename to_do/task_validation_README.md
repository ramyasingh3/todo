# Task Validation

## Feature Description
The Task Validation feature provides comprehensive validation for task properties, ensuring data integrity and consistency across the task management system. It validates task names, descriptions, priorities, due dates, and tags according to predefined rules.

## Validation Rules

### Task Name
- Minimum length: 3 characters
- Maximum length: 100 characters
- Cannot be empty or contain only whitespace
- Only allowed characters: letters, numbers, spaces, and basic punctuation
- Cannot be a reserved word

### Task Description
- Optional field
- Maximum length: 500 characters
- Can contain any characters

### Task Priority
- Must be an integer
- Range: 1 to 5
- 1: Highest priority
- 5: Lowest priority

### Due Date
- Optional field
- Must be in YYYY-MM-DD format
- Must be a valid date

### Tags
- Optional field
- Each tag must be non-empty
- Maximum length per tag: 20 characters
- Only alphanumeric characters and hyphens allowed
- Case-sensitive

## Usage Examples

### Basic Usage
```python
from task_validation import TaskValidator

validator = TaskValidator()

# Validate a complete task
is_valid, errors = validator.validate_task(
    name="Complete project",
    description="Finish by Friday",
    priority=2,
    due_date="2024-03-15",
    tags=["work", "urgent"]
)

if is_valid:
    print("Task is valid")
else:
    print("Task validation failed:")
    for error in errors:
        print(f"- {error}")
```

### Individual Validation
```python
# Validate task name
is_valid, error = validator.validate_task_name("New Task")
print(f"Name valid: {is_valid}")
print(f"Error: {error}")

# Validate priority
is_valid, error = validator.validate_task_priority(3)
print(f"Priority valid: {is_valid}")
print(f"Error: {error}")
```

## Implementation Details

### TaskValidator Class
- Central class for all validation logic
- Configurable validation rules
- Methods for individual property validation
- Comprehensive error reporting

### Validation Methods
1. `validate_task_name()`: Validates task name format and content
2. `validate_task_description()`: Validates description length
3. `validate_task_priority()`: Validates priority range
4. `validate_task_due_date()`: Validates date format
5. `validate_task_tags()`: Validates tag format and content
6. `validate_task()`: Validates all properties at once

## Error Handling
- Each validation method returns a tuple of (is_valid, error_message)
- The main validate_task method returns (is_valid, list_of_errors)
- Error messages are descriptive and user-friendly
- Validation stops at the first error for each property

## Common Applications
- Task creation and editing
- Data import validation
- API request validation
- Form validation in UI
- Data integrity checks 