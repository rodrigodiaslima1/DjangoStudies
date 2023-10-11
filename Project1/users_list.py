
class Users:

    def __init__(self):
        print("===> Users Constructor")


    def find_user(self, users_list, username):
        for user in users_list:
            if(user["username"] == username):
                return user
        return "no user found ..."

    users_list = [
        {
            "username": "rodrigodiaslima1",
            "first_name": "rodrigo",
            "middle_name": "dias",
            "last_name": "lima"
        },
        {
            "username": "elzaaparecidadias1",
            "first_name": "elza",
            "middle_name": "aparecida",
            "last_name": "dias"
        },
        {
            "username": "rogerdaltron64",
            "first_name": "roger",
            "middle_name": "",
            "last_name": "daltron"
        }
    ]