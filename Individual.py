import pymongo

class Individual():
    """Someone that can be assigned chores/tasks."""
    def __init__(name=None):
        self.name = name