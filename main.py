from todo_service import TodoService

def print_menu():
    print("\n=== Todo List Application ===")
    print("1. Add new todo")
    print("2. List all todos")
    print("3. Mark todo as completed")
    print("4. Mark todo as incomplete")
    print("5. Update todo")
    print("6. Delete todo")
    print("7. Exit")
    print("===========================")

def main():
    service = TodoService()
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            title = input("Enter todo title: ")
            description = input("Enter todo description: ")
            try:
                todo = service.create_todo(title, description)
                print(f"Todo created successfully with ID: {todo.id}")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "2":
            todos = service.get_all_todos()
            if not todos:
                print("No todos found!")
            else:
                for todo in todos:
                    status = "✓" if todo.completed else " "
                    print(f"[{status}] {todo.id}. {todo.title} - {todo.description}")
                    
        elif choice == "3":
            todo_id = int(input("Enter todo ID to mark as completed: "))
            todo = service.mark_todo_completed(todo_id)
            if todo:
                print("Todo marked as completed!")
            else:
                print("Todo not found!")
                
        elif choice == "4":
            todo_id = int(input("Enter todo ID to mark as incomplete: "))
            todo = service.mark_todo_incomplete(todo_id)
            if todo:
                print("Todo marked as incomplete!")
            else:
                print("Todo not found!")
                
        elif choice == "5":
            todo_id = int(input("Enter todo ID to update: "))
            title = input("Enter new title (press Enter to skip): ")
            description = input("Enter new description (press Enter to skip): ")
            try:
                todo = service.update_todo(todo_id, title or None, description or None)
                if todo:
                    print("Todo updated successfully!")
                else:
                    print("Todo not found!")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "6":
            todo_id = int(input("Enter todo ID to delete: "))
            if service.delete_todo(todo_id):
                print("Todo deleted successfully!")
            else:
                print("Todo not found!")
                
        elif choice == "7":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 