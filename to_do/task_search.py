from typing import List, Optional, Union
from datetime import datetime

class Task:
    def __init__(self, name: str, description: str = "", priority: int = 3,
                 due_date: str = "", tags: List[str] = None, completed: bool = False):
        self.name = name
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.tags = tags or []
        self.completed = completed
        self.created_at = datetime.now()

    def __str__(self) -> str:
        status = "✓" if self.completed else " "
        return f"[{status}] {self.name} (Priority: {self.priority})"

class TaskSearch:
    def __init__(self, tasks: List[Task]):
        self.tasks = tasks

    def search_by_name(self, query: str, case_sensitive: bool = False) -> List[Task]:
        """
        Search tasks by name using substring matching.
        """
        if not case_sensitive:
            query = query.lower()
        
        return [
            task for task in self.tasks
            if query in (task.name if case_sensitive else task.name.lower())
        ]

    def search_by_description(self, query: str, case_sensitive: bool = False) -> List[Task]:
        """
        Search tasks by description using substring matching.
        """
        if not case_sensitive:
            query = query.lower()
        
        return [
            task for task in self.tasks
            if query in (task.description if case_sensitive else task.description.lower())
        ]

    def search_by_priority(self, priority: int) -> List[Task]:
        """
        Search tasks by priority level.
        """
        return [task for task in self.tasks if task.priority == priority]

    def search_by_due_date(self, start_date: Optional[str] = None,
                          end_date: Optional[str] = None) -> List[Task]:
        """
        Search tasks by due date range.
        """
        try:
            if start_date:
                start = datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                end = datetime.strptime(end_date, "%Y-%m-%d")
            
            return [
                task for task in self.tasks
                if task.due_date and (
                    (not start_date or datetime.strptime(task.due_date, "%Y-%m-%d") >= start) and
                    (not end_date or datetime.strptime(task.due_date, "%Y-%m-%d") <= end)
                )
            ]
        except ValueError:
            return []

    def search_by_tags(self, tags: List[str], match_all: bool = True) -> List[Task]:
        """
        Search tasks by tags.
        If match_all is True, all tags must be present.
        If match_all is False, any tag can be present.
        """
        if not tags:
            return self.tasks
        
        if match_all:
            return [
                task for task in self.tasks
                if all(tag in task.tags for tag in tags)
            ]
        else:
            return [
                task for task in self.tasks
                if any(tag in task.tags for tag in tags)
            ]

    def search_by_status(self, completed: bool) -> List[Task]:
        """
        Search tasks by completion status.
        """
        return [task for task in self.tasks if task.completed == completed]

    def advanced_search(self, name: Optional[str] = None,
                       description: Optional[str] = None,
                       priority: Optional[int] = None,
                       start_date: Optional[str] = None,
                       end_date: Optional[str] = None,
                       tags: Optional[List[str]] = None,
                       match_all_tags: bool = True,
                       completed: Optional[bool] = None) -> List[Task]:
        """
        Perform an advanced search combining multiple criteria.
        """
        results = self.tasks

        if name:
            results = self.search_by_name(name)
        if description:
            results = [task for task in results if task in self.search_by_description(description)]
        if priority is not None:
            results = [task for task in results if task in self.search_by_priority(priority)]
        if start_date or end_date:
            results = [task for task in results if task in self.search_by_due_date(start_date, end_date)]
        if tags:
            results = [task for task in results if task in self.search_by_tags(tags, match_all_tags)]
        if completed is not None:
            results = [task for task in results if task in self.search_by_status(completed)]

        return results

def test_search():
    # Create sample tasks
    tasks = [
        Task("Complete project", "Finish the project by Friday", 2, "2024-03-15", ["work", "urgent"]),
        Task("Buy groceries", "Milk, eggs, bread", 3, "2024-03-10", ["shopping"]),
        Task("Call mom", "Wish her happy birthday", 1, "2024-03-08", ["personal", "urgent"]),
        Task("Exercise", "30 minutes of cardio", 4, "2024-03-20", ["health"]),
        Task("Read book", "Chapter 5 of Python book", 3, "2024-03-25", ["learning"]),
    ]
    
    search = TaskSearch(tasks)
    
    # Test Case 1: Search by name
    print("Test Case 1: Search by name")
    results = search.search_by_name("project")
    for task in results:
        print(task)
    print()
    
    # Test Case 2: Search by priority
    print("Test Case 2: Search by priority")
    results = search.search_by_priority(3)
    for task in results:
        print(task)
    print()
    
    # Test Case 3: Search by due date range
    print("Test Case 3: Search by due date range")
    results = search.search_by_due_date("2024-03-10", "2024-03-15")
    for task in results:
        print(task)
    print()
    
    # Test Case 4: Search by tags
    print("Test Case 4: Search by tags")
    results = search.search_by_tags(["urgent"], match_all=True)
    for task in results:
        print(task)
    print()
    
    # Test Case 5: Advanced search
    print("Test Case 5: Advanced search")
    results = search.advanced_search(
        name="project",
        priority=2,
        tags=["work"],
        match_all_tags=True
    )
    for task in results:
        print(task)

if __name__ == "__main__":
    test_search() 