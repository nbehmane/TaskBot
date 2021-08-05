import pymongo

class User():
    """Someone that can be assigned chores/tasks."""
    def __init__(name=None):
        """Initialize a user."""
        self.name = name
    