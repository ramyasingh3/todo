import heapq
from datetime import datetime

class Task:
    def __init__(self, description, priority=0, due_date=None):
        """
        Initialize a task with description, priority, and optional due date.
        
        Args:
            description (str): Task description
            priority (int): Task priority (0 = lowest, higher numbers = higher priority)
            due_date (str): Optional due date in format 'YYYY-MM-DD'
        """
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.created_at = datetime.now()
        self.completed = False

    def __lt__(self, other):
        """
        Compare tasks based on priority and due date.
        Higher priority tasks come first.
        For same priority, earlier due dates come first.
        """
        if self.priority != other.priority:
            return self.priority > other.priority
        if self.due_date and other.due_date:
            return self.due_date < other.due_date
        return self.created_at < other.created_at

class TaskPriorityQueue:
    def __init__(self):
        """Initialize an empty priority queue for tasks."""
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, priority=0, due_date=None):
        """
        Add a new task to the priority queue.
        
        Args:
            description (str): Task description
            priority (int): Task priority
            due_date (str): Optional due date
        """
        task = Task(description, priority, due_date)
        heapq.heappush(self.tasks, task)
        return task

    def get_next_task(self):
        """
        Get and remove the highest priority task from the queue.
        
        Returns:
            Task: The highest priority task, or None if queue is empty
        """
        if not self.tasks:
            return None
        return heapq.heappop(self.tasks)

    def complete_task(self, task):
        """
        Mark a task as completed and move it to completed tasks.
        
        Args:
            task (Task): The task to mark as completed
        """
        task.completed = True
        task.completed_at = datetime.now()
        self.completed_tasks.append(task)

    def get_all_tasks(self):
        """
        Get all tasks in priority order without removing them.
        
        Returns:
            list: List of tasks in priority order
        """
        return sorted(self.tasks, reverse=True)

    def get_completed_tasks(self):
        """
        Get all completed tasks.
        
        Returns:
            list: List of completed tasks
        """
        return self.completed_tasks

    def clear_completed_tasks(self):
        """Clear all completed tasks."""
        self.completed_tasks = []

    def __str__(self):
        """Return a string representation of the task queue."""
        result = "Current Tasks:\n"
        for task in sorted(self.tasks, reverse=True):
            status = "Completed" if task.completed else "Pending"
            due_date = f", Due: {task.due_date}" if task.due_date else ""
            result += f"- {task.description} (Priority: {task.priority}{due_date}, Status: {status})\n"
        
        if self.completed_tasks:
            result += "\nCompleted Tasks:\n"
            for task in self.completed_tasks:
                result += f"- {task.description} (Completed at: {task.completed_at})\n"
        
        return result

# Test cases
if __name__ == "__main__":
    # Create a task queue
    task_queue = TaskPriorityQueue()
    
    # Add some tasks
    task1 = task_queue.add_task("Complete project documentation", priority=2, due_date="2024-04-10")
    task2 = task_queue.add_task("Review pull requests", priority=1)
    task3 = task_queue.add_task("Fix critical bug", priority=3, due_date="2024-04-08")
    task4 = task_queue.add_task("Update dependencies", priority=1, due_date="2024-04-15")
    
    print("Initial task queue:")
    print(task_queue)
    
    # Complete some tasks
    task_queue.complete_task(task3)
    task_queue.complete_task(task2)
    
    print("\nAfter completing tasks:")
    print(task_queue)
    
    # Get next task
    next_task = task_queue.get_next_task()
    print(f"\nNext task to work on: {next_task.description}")
    
    print("\nRemaining tasks:")
    print(task_queue)
    
    # Clear completed tasks
    task_queue.clear_completed_tasks()
    print("\nAfter clearing completed tasks:")
    print(task_queue) 