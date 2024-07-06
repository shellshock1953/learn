from class_admin import Admin
from class_user import User

default_admin = Admin("default_admin", ['get_user_list'])
default_admin.greeting()
default_admin.privileges.show_privileges()

andrew = User("Andrew")
andrew.greeting()

tommy = Admin("Tommy", ['add_user', 'update_pass'])
tommy.greeting()
tommy.privileges.show_privileges()
