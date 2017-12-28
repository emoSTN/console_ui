class Validator:

    def __init__(self, func, args=None):
        self.func = func
        self.args = args

    def call_func(self, value):
        if not value:
            return True
        return self.func(value, *self.args) if self.args else self.func(value)
