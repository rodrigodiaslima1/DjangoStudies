
from Project1.users_list import *

users = Users()
users_list = users.users_list

result = users.find_user(users_list, "rodrigodiaslima1")
print(result)