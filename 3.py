def login(username, password):
    correct_username = "Kage"
    correct_password = "7777777"
    assert username == correct_username, "Invalid username or password"
    assert password == correct_password, "Invalid username or password"
    print("Login successful")
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")
try:
    login(user_input_username, user_input_password)
except AssertionError as e:
    print(f"Error: {e}")
