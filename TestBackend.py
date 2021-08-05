from User import User
from User import UserRepo
import dotenv
config = dotenv.dotenv_values(".env")

def test_test():
    print("Test script running...")

def test_repo_create():
    repo = UserRepo(mongo_url=config["MONGO_URL"])
    if repo.create("Nima", ["Dishes"]) == True:
        print("Test Create...Worked...")

def test_repo_read():
    repo = UserRepo(mongo_url=config["MONGO_URL"])
    user = repo.read(user_name="Nima")
    if user[0]["name"] == "Nima":
        print("{}".format(user[0]["name"]))

def test_repo_make_user_object():
    repo = UserRepo(mongo_url=config["MONGO_URL"])
    user_from_database = repo.read(user_name="Nima")
    user_object = User(user_from_database[0])
    print(user_object)
    
def main():
    test_test()
    test_repo_read()
    test_repo_make_user_object()

if __name__ == "__main__":
    main()