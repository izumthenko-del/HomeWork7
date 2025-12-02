def check_age(age):
    assert age >= 18, "You must be 18 years old or older"
    print("You can use this service")
user_input = input("Please enter your age:")
try:
    user_age = int(user_input)
    check_age(user_age)
except ValueError:
    print("Error: Please enter a valid numerical age.")
except AssertionError as e:
    print(e)
