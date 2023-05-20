#! /usr/bin/python3

from users import User
import getpass
import sys
import json


def register():
    """
    This function is used for user registration.
    The username should not be duplicated.
    The entered password should be equal to or greater than 4 characters in length.
    """
    user_name = input("Enter username: ")
    if user_name in User.users_name:
        print("This username is already taken")
        return

    password = getpass.getpass(stream=sys.stderr, prompt="Enter Password : ")
    phone = input("Enter phone (optional): ")
    if User.sign_up(user_name, password, phone) != 0:
        User.users[user_name] = User(user_name, password, phone)
        User.users_json[user_name] = {"name": user_name, "password": password, "phone": phone}
        print(f"User {user_name} created successfully.")

        # storing to the json file
        json_string = json.dumps(User.users_json)
        with open("data.json", "w") as f:
            f.write(json_string)
    else:
        print("^" * 60, "Not Registered Please Enter Valid Values !!!", sep="\n")


def edit(username: str):
    """
    This function is used to edit the name and phone number of a user who has previously registered.
    """
    print("-" * 30, "Edit Menu!", "-" * 30, sep="\n")
    new_user_name = input("Enter new user name : ")
    if new_user_name != "":
        User.users[username].user_name = new_user_name
    new_phone = input("Enter new phone number : ")
    if new_phone != "":
        User.users[username].phone = new_phone

    if new_user_name != "":
        User.users[new_user_name] = User.users[username]
        User.users.pop(username)
        login(new_user_name)
    else:
        login(username)


def change_password(user_name: str):
    """
    This function is used to change the user's password.
    Note: that for greater security, the password you type will not be displayed.
    """
    old_pass = getpass.getpass(stream=sys.stderr, prompt="old password : ")
    new_password = getpass.getpass(stream=sys.stderr, prompt="new password : ")
    confirm_new_password = getpass.getpass(stream=sys.stderr, prompt="confirm new password : ")
    if new_password == confirm_new_password:
        User.change_password(user_name, old_pass, new_password)
    else:
        print("New passwords must match")
        change_password(user_name)

    login(user_name)


def login(username=None):
    """
    This function is used for registering a new user.
    The username should not be duplicated.
    The entered password will not be displayed.
    """
    if username is None:
        username = input("Enter username: ")
        if username not in User.users:
            print("Invalid username")
            return
        password = getpass.getpass(stream=sys.stderr, prompt="Enter Password : ")
        user = User.users[username]
        if not user.get_password(password):
            print("Invalid password")
            return

    print("-" * 30, "\tLogin Menu", "-" * 30, sep="\n")
    print("Please select an option:",
          "1. Show Your Specifications",
          "2. Edit",
          "3. Change Password",
          "4. Exit",
          sep="\n")
    print("-" * 30)
    choice = input(">>> ")
    match choice:
        case "1":
            print(User.users[username])
            login(username)
        case "2":
            edit(username)
        case "3":
            change_password(username)
        case "4":
            return


def main():
    """
    This function is the main function of the program used to display
    the main menu to the user for registering or editing user information.
    """
    while True:
        print("-" * 30, "\tMain Menu", "-" * 30, sep="\n")
        print("Please select an option:",
              "0. Exit",
              "1. Register",
              "2. Login",
              sep="\n")

        choice = input(">>> ")

        match choice:
            case "0":
                break
            case "1":
                register()
                continue
            case "2":
                login()
                continue


if __name__ == "__main__":
    main()