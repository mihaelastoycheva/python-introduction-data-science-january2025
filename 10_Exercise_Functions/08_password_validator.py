# def password_validator(password: str) -> None:
#     is_valid = True
#
#     if not (6 <= len(password) <= 10):
#         print("Password must be between 6 and 10 characters")
#         is_valid = False
#
#     if not password.isalnum():
#         print("Password must consist only of letters and digits")
#         is_valid = False
#
#     digit_count = sum(char.isdigit() for char in password)
#     if digit_count < 2:
#         print("Password must have at least 2 digits")
#         is_valid = False
#
#     if is_valid:
#         print("Password is valid")
#
#
# input_password = input()
# password_validator(input_password)

# --------------------------------- 2nd solution:

def password_validator(password: str) -> str:
    result = ""

    if not (6 <= len(password) <= 10):
        result += "Password must be between 6 and 10 characters\n"

    if not password.isalnum():
        result += "Password must consist only of letters and digits\n"

    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        result += "Password must have at least 2 digits"

    if not result:
        result += "Password is valid"

    return result


input_password = input()
print(password_validator(input_password))
