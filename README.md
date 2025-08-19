# Todo List Application

A simple command-line todo list application written in Python.

This repository contains a small CLI tool and supporting modules. Recent updates focus on general maintenance, documentation polish, and minor refactors to keep things tidy and easy to run.

## Features

- Create new todos with title and description
- List all todos
- Mark todos as completed/incomplete
- Update existing todos
- Delete todos
- Simple command-line interface

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd to_do_list_project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

Follow the on-screen menu to:
1. Add new todos
2. List all todos
3. Mark todos as completed
4. Mark todos as incomplete
5. Update existing todos
6. Delete todos
7. Exit the application

## Development

The project follows a simple layered architecture:
- `todo_model.py`: Contains the Todo data model
- `todo_repository.py`: Handles data persistence
- `todo_service.py`: Contains business logic
- `main.py`: Command-line interface

Contributions: If you notice an opportunity for a small improvement (docs, tests, or code clarity), feel free to open an issue or a PR.

## Testing

Run tests using pytest:
```bash
pytest
```

## Code Style

The project uses:
- Black for code formatting
- Flake8 for linting

Run formatting:
```bash
black .
```

Run linting:
```bash
flake8
``` 