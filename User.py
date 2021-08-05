from pymongo import MongoClient

class UserRepo():
    """The user repository to interface with MongoDB."""
    def __init__(self, mongo_url):
        """Initializes the interface to the MongoDB"""
        self.client = MongoClient(mongo_url)
        self.database = self.client['Users']
        self.collection = self.database['UserInformation']
    
    def create(self, user):
        """Create a User in the database given a user object."""
        pass
    def  read(self, user=None):
        """Read the database for users, or a specific user 
            given a User object"""
        pass
    def update(self, user):
        """Updates a user in the database given a User object."""
        pass
    def delete(self, user):
        """Delete a user from the database given a User object."""
        pass
    

class User():
    """Someone that can be assigned chores/tasks."""
    def __init__(name=None, tasks=[]):
        """Initialize a user."""
        self.name = name
        self.tasks = tasks


    