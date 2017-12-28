def is_number(val):
    if not val:
        return True
    try:
        int(val)
        return True
    except ValueError:
        return False


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
