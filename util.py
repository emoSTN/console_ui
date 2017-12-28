import base64
import getpass
import os
import urllib
import urlparse

from fake_useragent import UserAgent
from tkinter import *

if sys.version_info < (3, 0):
    try:
        input = raw_input
    except NameError:
        pass

ua = UserAgent()


class Validator:

    def __init__(self, func, args=None):
        self.func = func
        self.args = args

    def call_func(self, value):
        if not value:
            return True
        return self.func(value, *self.args) if self.args else self.func(value)


def encode(plain):
    return base64.b64encode(plain)


def decode(encoded):
    return base64.b64decode(encoded)


def encode_basic_auth(username, password):
    return base64.b64encode('%s:%s' % (username, password))


def decode_basic_auth(encoded):
    return tuple(base64.b64decode(encoded).split(':'))


def build_url(base, path, args_dict=None):
    # Returns a list in the structure of urlparse.ParseResult
    url_parts = list(urlparse.urlparse(base))
    url_parts[2] = path
    if args_dict:
        url_parts[4] = urllib.urlencode(args_dict)
    return urlparse.urlunparse(url_parts)


def user_input(label, validation, *args):
    while True:
        inp = input(label)
        if validation is None or validation(inp, *args):
            return inp
        elif validation(inp, *args) is None:
            return None
        print('Invalid input')


def validated_user_input(label, validators):
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


def path_validation(val):
    if not val:
        return True
    try:
        os.makedirs(val)
        return True
    except OSError:
        return os.path.exists(val) and os.path.isdir(val)


def is_number(val):
    if not val:
        return True
    try:
        int(val)
        return True
    except ValueError:
        return False


def not_blank(val):
    return val is not None and len(val) > 0


def is_blank(val):
    return val is None or len(val) == 0


def encode_json_list(json_list):
    return [el.encode('utf-8') for el in json_list]


def pass_input():
    label = 'Enter password: '
    while True:
        if sys.stdin.isatty():
            inp = getpass.getpass(label)
        else:
            inp = input(label)
        if not_blank(inp):
            return encode(inp)
        print('Password must not be empty')


def number_in_range(val, x, y):
    if not val:
        return True
    try:
        val = int(val)
    except ValueError:
        return True
    if x is None or y is None or y < 1:
        return False
    return val in range(x, y)
