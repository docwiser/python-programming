import random
import os
current_user = None
def createAccount():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    gender = input("Enter your gender: ")
    password = input("Enter your password or 0 to auto-generate: ")
    if password == "0":
        password = str(random.randint(100000, 999999))
        print(f"Auto generated password: {password}. Please remember it")
    if existingEmail(email):
        print("Sorry, that email is already in use. Please try with a different email.")
        return
    user = {
        "name": name,
        "email": email,
        "gender": gender,
        "password": password
    }
    saveUser(user, 1)
def saveUser(user, arg):
    users = readUsers()
    updated = False
    for i, u in enumerate(users):
        if u["email"] == user["email"]:
            users[i] = user
            updated = True
            break
    if not updated:
        users.append(user)
    with open("users.txt", "w") as f:
        for u in users:
            f.write(f'{u["name"]}|{u["email"]}|{u["gender"]}|{u["password"]}\n')
    if arg == 1:
        print("Your account has been created successfully!")
    else:
        print("Your account has been updated successfully!")
def readUsers():
    if not os.path.exists("users.txt"):
        return []
    with open("users.txt", "r") as f:
        lines = f.readlines()

    users = []
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 4:
            users.append({
                "name": parts[0],
                "email": parts[1],
                "gender": parts[2],
                "password": parts[3]
            })
    return users
def existingEmail(email):
    users = readUsers()
    for user in users:
        if user["email"] == email:
            return True
    return False
def login():
    global current_user
    if current_user:
        print(f"Already logged in as {current_user['email']}")
        return

    email = input("Enter your email: ")
    password = input("Enter your password: ")
    users = readUsers()

    for user in users:
        if user["email"] == email and user["password"] == password:
            current_user = user
            print(f"Login successful! Welcome, {user['name']}")
            return

    print("Invalid email or password.")
def logout():
    global current_user
    if current_user:
        print(f"User {current_user['email']} logged out.")
        current_user = None
    else:
        print("No user is currently logged in.")
def editProfile():
    global current_user
    if not current_user:
        print("You must be logged in to edit your profile.")
        return

    print("Leave field blank to keep current value.")
    name = input(f"New name ({current_user['name']}): ") or current_user['name']
    gender = input(f"New gender ({current_user['gender']}): ") or current_user['gender']

    current_user["name"] = name
    current_user["gender"] = gender
    saveUser(current_user, 0)
def changePassword():
    global current_user
    if not current_user:
        print("You must be logged in to change your password.")
        return

    old = input("Enter your current password: ")
    if old != current_user["password"]:
        print("Incorrect current password.")
        return

    new = input("Enter new password: ")
    current_user["password"] = new
    saveUser(current_user, 0)
def menu():
    print("""
--- Account Management System ---
1. Create Account
2. Login
3. Logout
4. Edit Profile
5. Change Password
6. Exit
""")
def main():
    while True:
        menu()
        choice = input("Choose an option (1-6): ")
        if choice == "1":
            createAccount()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            editProfile()
        elif choice == "5":
            changePassword()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
