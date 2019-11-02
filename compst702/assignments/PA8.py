# This program helps to set a password.
# This function returns True if the string s has
# no lowercase character otherwise returns False.


def noLowercase(s):
    upper_s = s.upper()
    if s == upper_s:
        return True
    else:
        return False


# This function returns True if the string s has 
# no uppercase character otherwise returns False.
def noUppercase(s):
    lower_s = s.lower()
    if s == lower_s:
        return True
    else:
        return False


# This function returns True if the string s has 
# no digit character otherwise returns False.
def noDigit(s):
    if s.count("0") > 0:
        return False
    elif s.count("1") > 0:
        return False
    elif s.count("2") > 0:
        return False
    elif s.count("3") > 0:
        return False
    elif s.count("4") > 0:
        return False
    elif s.count("5") > 0:
        return False
    elif s.count("6") > 0:
        return False
    elif s.count("7") > 0:
        return False
    elif s.count("8") > 0:
        return False
    elif s.count("9") > 0:
        return False
    else:
        return True


def lengthFail(s):
    if len(s) < 8:
        return True
    else:
        return False


def passCheck(s):
    if not noDigit(s) and not noUppercase(s) and not noLowercase(s) and not lengthFail(s):
        return True


# Program to set a password.
# The password must have more than 8 characters
# with at least one uppercase, at least one lowercase
# and at least one digit character.
def main():
    print("This program will set your password.")
    password_not_set = True
    while password_not_set:
        password = input("Enter a password: ")
        valid_password = passCheck(password)
        while not valid_password:
            print("Password not allowed.")
            print("Must be longer than 8 characters with")
            print("at least one lowercase, one uppercase and one digit.\n")
            password = input("Enter another password: ")
            valid_password = passCheck(password)
        password_confirm = input("Reenter to confirm the password. ")
        if password_confirm != password:
            print("Password did not match, please set another password.")
        else:
            print("Your password has been set.")
            password_not_set = False

        
main()
