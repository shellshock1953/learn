import json
filename = 'greet_user.json'

def get_stored_username():
    """Get username from file, or return None"""
    try:
       with open(filename, 'r') as f:
           # username = f.read().rstrip()
           username = json.load(f)
           return username
    except FileNotFoundError:
        # new user
        return None

def create_new_user():
    """Get username as an input, store it to file"""
    username = input("Your name:")
    print(f"I`ll remember you, {username}")
    with open(filename, 'w') as f:
        json.dump(username, f)

def confirm_username(username):
    # corrent_responce = False
    # while not corrent_responce:
    while True:
        confirm = input(f"Are U {username}? [Y/n]")
        if confirm in ['Y','y','yes']:
            # corrent_responce = True
            return True
        elif confirm in ['N','n','no']:
            # corrent_responce = True
            return False
        else:
            print(f"Repsond with Y or N only")

def greet_user():
    """Green user, if present, or create a new one"""
    username = get_stored_username()
    if username:
        # user already present
        if confirm_username(username):
            print(f"Greeting {username}")
        else:
            create_new_user()

    else:
        # new user
        create_new_user()

greet_user()
