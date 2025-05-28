class Todo:
    def __init__(self, id, title, description, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = None
        self.updated_at = None

    def mark_completed(self):
        self.completed = True
        self.updated_at = None  # This would be set to current timestamp in real app

    def mark_incomplete(self):
        self.completed = False
        self.updated_at = None  # This would be set to current timestamp in real app

    def update_title(self, new_title):
        self.title = new_title
        self.updated_at = None  # This would be set to current timestamp in real app

    def update_description(self, new_description):
        self.description = new_description
        self.updated_at = None  # This would be set to current timestamp in real app 