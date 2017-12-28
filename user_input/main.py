import getpass
import sys

from user_input import validations

if sys.version_info < (3, 0):
    try:
        input = raw_input
    except NameError:
        pass


def user_input(label, validators):
    while True:
        inp = input(label)
        check = True
        if not validators:
            return inp
        for validator in validators:
            check = check and validator.call_func(inp)
            if not check:
                print('Invalid input')
                break
        if check:
            return inp


def pass_input():
    label = 'Enter password: '
    while True:
        if sys.stdin.isatty():
            inp = getpass.getpass(label)
        else:
            inp = input(label)
        if validations.not_blank(inp):
            return inp
        print('Password must not be empty')
