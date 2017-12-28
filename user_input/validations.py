import os


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
