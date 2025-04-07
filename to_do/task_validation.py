class TaskValidator:
    def __init__(self):
        self.min_length = 3
        self.max_length = 100
        self.allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?-()")
        self.reserved_words = {"none", "null", "undefined", "empty", "invalid"}

    def validate_task_name(self, name: str) -> tuple[bool, str]:
        """
        Validates a task name using multiple criteria.
        Returns (is_valid, error_message)
        """
        # Check length
        if len(name) < self.min_length:
            return False, f"Task name must be at least {self.min_length} characters long"
        if len(name) > self.max_length:
            return False, f"Task name must not exceed {self.max_length} characters"

        # Check for empty or whitespace-only names
        if not name.strip():
            return False, "Task name cannot be empty or contain only whitespace"

        # Check for invalid characters
        invalid_chars = set(name) - self.allowed_chars
        if invalid_chars:
            return False, f"Task name contains invalid characters: {', '.join(invalid_chars)}"

        # Check for reserved words
        if name.lower() in self.reserved_words:
            return False, "Task name cannot be a reserved word"

        return True, ""

    def validate_task_description(self, description: str) -> tuple[bool, str]:
        """
        Validates a task description.
        Returns (is_valid, error_message)
        """
        if not description:
            return True, ""  # Description is optional

        if len(description) > 500:
            return False, "Description must not exceed 500 characters"

        return True, ""

    def validate_task_priority(self, priority: int) -> tuple[bool, str]:
        """
        Validates a task priority.
        Returns (is_valid, error_message)
        """
        if not isinstance(priority, int):
            return False, "Priority must be an integer"
        if priority < 1 or priority > 5:
            return False, "Priority must be between 1 and 5"
        return True, ""

    def validate_task_due_date(self, due_date: str) -> tuple[bool, str]:
        """
        Validates a task due date.
        Returns (is_valid, error_message)
        """
        if not due_date:
            return True, ""  # Due date is optional

        try:
            from datetime import datetime
            datetime.strptime(due_date, "%Y-%m-%d")
            return True, ""
        except ValueError:
            return False, "Due date must be in YYYY-MM-DD format"

    def validate_task_tags(self, tags: list[str]) -> tuple[bool, str]:
        """
        Validates task tags.
        Returns (is_valid, error_message)
        """
        if not tags:
            return True, ""  # Tags are optional

        for tag in tags:
            if not tag.strip():
                return False, "Tags cannot be empty or contain only whitespace"
            if len(tag) > 20:
                return False, f"Tag '{tag}' exceeds maximum length of 20 characters"
            if not all(c.isalnum() or c == '-' for c in tag):
                return False, f"Tag '{tag}' contains invalid characters. Only alphanumeric characters and hyphens are allowed"

        return True, ""

    def validate_task(self, name: str, description: str = "", priority: int = 3, 
                     due_date: str = "", tags: list[str] = None) -> tuple[bool, list[str]]:
        """
        Validates all task properties at once.
        Returns (is_valid, error_messages)
        """
        errors = []
        
        # Validate name
        is_valid, error = self.validate_task_name(name)
        if not is_valid:
            errors.append(f"Name: {error}")
        
        # Validate description
        is_valid, error = self.validate_task_description(description)
        if not is_valid:
            errors.append(f"Description: {error}")
        
        # Validate priority
        is_valid, error = self.validate_task_priority(priority)
        if not is_valid:
            errors.append(f"Priority: {error}")
        
        # Validate due date
        is_valid, error = self.validate_task_due_date(due_date)
        if not is_valid:
            errors.append(f"Due Date: {error}")
        
        # Validate tags
        is_valid, error = self.validate_task_tags(tags or [])
        if not is_valid:
            errors.append(f"Tags: {error}")
        
        return len(errors) == 0, errors

def test_validator():
    validator = TaskValidator()
    
    # Test Case 1: Valid task
    print("Test Case 1: Valid task")
    is_valid, errors = validator.validate_task(
        name="Complete project",
        description="Finish the project by Friday",
        priority=2,
        due_date="2024-03-15",
        tags=["work", "urgent"]
    )
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")
    print()
    
    # Test Case 2: Invalid name
    print("Test Case 2: Invalid name")
    is_valid, errors = validator.validate_task(
        name="a",  # Too short
        description="Valid description",
        priority=3,
        due_date="2024-03-15",
        tags=["work"]
    )
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")
    print()
    
    # Test Case 3: Invalid priority
    print("Test Case 3: Invalid priority")
    is_valid, errors = validator.validate_task(
        name="Valid task",
        description="Valid description",
        priority=6,  # Out of range
        due_date="2024-03-15",
        tags=["work"]
    )
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")
    print()
    
    # Test Case 4: Invalid due date
    print("Test Case 4: Invalid due date")
    is_valid, errors = validator.validate_task(
        name="Valid task",
        description="Valid description",
        priority=3,
        due_date="2024/03/15",  # Wrong format
        tags=["work"]
    )
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")
    print()
    
    # Test Case 5: Invalid tags
    print("Test Case 5: Invalid tags")
    is_valid, errors = validator.validate_task(
        name="Valid task",
        description="Valid description",
        priority=3,
        due_date="2024-03-15",
        tags=["work!", "very_long_tag_name_that_exceeds_limit"]  # Invalid characters and length
    )
    print(f"Valid: {is_valid}")
    print(f"Errors: {errors}")

if __name__ == "__main__":
    test_validator() 