USERS = {'user1': 'password1', 'user2': 'password2'}
print("\n")
name_input = input("Enter username: ")
pass_input = input("Enter password: ")

if name_input in USERS and USERS[name_input] == pass_input:
    

    print("Login successful!")
else:

    print("Error: Invalid username or password.")
