#! /usr/bin/python3

import uuid


class User:
    """
    The User class model is used to create a user instance when registering,
    and has the attributes of username, password, ID, and phone number.
    """
    users_name = []
    users = {}
    users_json = {}

    def __init__(self, user_name: str, password: str, phone: str = None):
        """
        Initializing a new instance of the User class.
        """
        self.user_name = user_name
        self.__password = password
        self.phone = phone
        self.user_id = uuid.uuid4().hex
        User.users_name.append(self.user_name)

    def get_password(self, password: str):
        """
        This function returns the password value of an instance
        that has been created from the User class and is private.
        """
        if self.__password == password:
            return True
        return False

    @classmethod
    def sign_up(cls, user_name: str, password: str, phone: str = None):
        """
        This function is a method class used to create a new user and also validates the received values.
        """
        if user_name not in cls.users_name and user_name != "" and len(password) >= 4:
            return cls(user_name, password, phone)
        return 0

    @staticmethod
    def change_password(user_name: str, old_password: str, new_password: str):
        """
        This method is used to change the password of an instance created from the User class.
        """
        user = User.users[user_name]
        if user.__password == old_password:
            user.__password = new_password
            print("\nPassword changed successfully!!!")
        else:
            print("\nInvalid password!")

    def __str__(self):
        """
        This method is used to print the custom values of instances of the User class.
        """
        return f"name : {self.user_name} | phone : {self.phone} | id : {self.user_id}"
