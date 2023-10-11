
from Project1.users_list import *

users = Users()



"""
The way we access lists and dictionaries in python
not necessarily is the same in Jinja

Accessing throught Jinja we use the dot (.)
{% for user in users_list_key %}

            <ul>
                <li>Username: {{ user.username }}</li>
                <li>First Name: {{ user.first_name }}</li>
                <li>Middle Name: {{ user.middle_name }}</li>
                <li>Last Name: {{ user.last_name }}</li>
                <br>
            </ul>
"""

username0 = users.users_list[0]["username"]
firstname0 = users.users_list[0]["first_name"]
middlename0 = users.users_list[0]["middle_name"]
lastname0 = users.users_list[0]["last_name"]



print(username0)
print(firstname0)
print(middlename0)
print(lastname0)

