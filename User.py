from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class UserRepo():
    """The user repository to interface with MongoDB."""

    def __init__(self, mongo_url=None):
        """Initializes the interface to the MongoDB given a Mongo URL."""
        self.client = MongoClient(mongo_url)
        self.database = self.client['Users']
        self.collection = self.database['UserInformation']
    
    def create(self, name, tasks=[]):
        """Create a User in the database given a user object."""
        self.collection.insert_one({"name": name, "tasks": tasks})
        return True

    def  read(self, user_name=None):
        """Read the database for users, or a specific user 
            given a User object.
            1. If a user_name is given, all users with that name 
                will be reuturned.
            2. If a user_name is not given, will return all users in database.
        """
        if user_name != None:
            return self.collection.find({"name": user_name})
        else:
            return self.collection.find({})
        

    def update(self, user):
        """Updates a user in the database given a User object."""
        pass

    def delete(self, user):
        """Delete a user from the database given a User object."""
        pass
    

class User():
    """Someone that can be assigned chores/tasks."""
    def __init__(self, bson_object):
        """Initialize a user."""
        self.name = bson_object["name"]
        self.tasks = bson_object["tasks"]
    
    def __repr__(self):
        return str(self.__dict__)
    


    