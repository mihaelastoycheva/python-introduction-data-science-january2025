PASSWORD = "s3cr3t!"

input_password = input()

# if input_password is "s3cr3t!":    -> "is" - in specific cases

if input_password == PASSWORD:
    print("Welcome")
else:
    print("Wrong password!")
