import re


def validate_email(email):
    # this will check if the email consists of only letters, numbers, underscores, periods, plus signs, and dashes
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False
    return True


def validate_password(password):
    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password) or " " in password:
        return False
    return True
