from User import User
from User import UserRepo
from dotenv import load_dotenv

def test_test():
    print("Test script running...")
def test_repo_create():
    repo = UserRepo(mongo_url=MONGO_URL)
    if repo != True:
        raise Exception
    else:
        return True

def main():
    test_test()

if __name__ == "__main__":
    main()