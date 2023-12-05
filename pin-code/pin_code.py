import sys

def user_pin_code():
    pin = 1111
    return pin


def user_enter_pin_code():
    pin = user_pin_code()
    user_attempts = 3

    for i in range(user_attempts):
        user_input = int(input("Hello, please enter your pin code: "))
        if user_input == pin:
            print("Pin code is correct.")
            break
        else:
            attempts_left = user_attempts - i - 1
            if attempts_left > 0:
                print(f"Incorrect pin code. You have {attempts_left} attempts left.")
            else:
                print("Sorry, you've run out of attempts. Your account is locked.")
                sys.exit()


# Виклик функцій
user_enter_pin_code()
