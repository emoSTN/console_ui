import getpass
import re
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


class NotBlank(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        while True:
            res = self.func(*args, **kwargs)
            if not res or res is None or re.match('/\A\s*\z/', res):
                print('Invalid input')
            else:
                break


class Size(object):
    def __init__(self, size):
        self.size = size

    def __call__(self, func):
        print "Inside __call__()"

        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.size)
            func(*args, **kwargs)
            print("After f(*args)")

        return wrapped_f


@NotBlank
def d_user_input(label):
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


def main():
    print(user_input('Test input', validators))


if __name__ == '__main__':
    main()
