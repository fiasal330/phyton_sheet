import json

users = [
    {"username": "Mohamed", "password": "1234#"},
    {"username": "AHMED", "password": "5678*"},
    {"username": "Sayed", "password": "0987"},
    {"username": "Omar", "password": "01194"}
]
My_file = open('users.json', 'w')
json.dump(users, My_file)
My_file.close()

#2 Write a program that read the JSON file and print the username and password of the first user.

My_file = open('users.json', 'r')
users = json.load(My_file)
My_file.close()
print(f"First user: {users[0]['username']} , pass: {users[0]['password']}")


# 3. Add new user
users.append({"username": "Ali", "password": "43gg#"})
My_file = open('users.json', 'w')
json.dump(users, My_file)
My_file.close()
print("User has been added")


# 4. check login 

u = input("Username: ")
p = input("Password: ")
My_file = open('users.json', 'r')
users = json.load(My_file)
My_file.close()

found = False
for user in users:
    if user['username'] == u and user['password'] == p:
        found = True
        break

print("Login Success!" if found else "Login Failed")