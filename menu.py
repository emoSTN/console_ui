import util


class FunctionItem:
    def __init__(self, label, func, args=None):
        self.label = label
        self.func = func
        self.args = args

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.__str__()

    def call_func(self):
        return self.func(*self.args) if self.args else self.func()


class ValueItem:
    def __init__(self, label, value):
        self.label = label
        self.value = value

    def __str__(self):
        return self.label

    def __repr__(self):
        return self.__str__()


class Menu:
    def __init__(self, items, default=0, title='MENU'):
        self.items = items
        self.default = default
        self.menu_heading = title
        self.stop = False
        self.selection = None
        self.max_str_len = 0
        self.margin_len = 1
        self.margin = ' ' * self.margin_len
        if not self.menu_validation():
            print('Invalid menu')
            exit('Terminating script')
        self.get_max_str_len()

    def stop(self):
        self.stop = True

    def get_max_str_len(self):
        for i in self.items[1:] + self.items[:1]:
            i_len = len('Selected: [%s]: %s' % (self.items.index(i), i.label))
            if i_len > self.max_str_len:
                self.max_str_len = i_len
        if len(self.menu_heading) > self.max_str_len:
            self.max_str_len = len(self.menu_heading)

    def print_heading(self):
        m1_len = self.max_str_len / 2 - (len(self.menu_heading) / 2)
        m1 = ' ' * m1_len
        m2_len = self.max_str_len - len(self.margin + m1 + self.menu_heading) + self.margin_len
        m2 = ' ' * m2_len
        print('\n')
        print(u'\u2554' + '=' * (self.max_str_len + self.margin_len * 2) + u'\u2557')
        print(u'\u2551' + self.margin + m1 + self.menu_heading + m2 + self.margin + u'\u2551')
        print(u'\u2560' + '=' * (self.max_str_len + self.margin_len * 2) + u'\u2563')

    def print_menu_list(self):
        for i in self.items[1:] + self.items[:1]:
            menu_str = '[%s]: %s' % (self.items.index(i), i.label)
            margin_len = self.max_str_len - len(menu_str)
            margin = ' ' * margin_len
            print(u'\u2551' + self.margin + menu_str + margin + self.margin + u'\u2551')
        print(u'\u2559' + '-' * (self.max_str_len + self.margin_len * 2) + u'\u255C')

    def print_selected(self, sel):
        sel_str = 'Selected: [%s]: %s' % (sel, self.items[sel].label)
        margin_len = self.max_str_len - len(sel_str)
        margin = ' ' * (margin_len + self.margin_len)
        print(u'\u2553' + '-' * (self.max_str_len + self.margin_len * 2) + u'\u2556')
        print(u'\u2551' + self.margin + sel_str + margin + u'\u2551')
        print(u'\u255A' + '=' * (self.max_str_len + self.margin_len * 2) + u'\u255D')
        print('\n')

    def select(self):
        if self.items is None:
            self.items = [FunctionItem('Exit', exit('Terminating script'))]
        while True and not self.stop:
            self.print_heading()
            self.print_menu_list()
            inp = util.validated_user_input(
                label='Please Select [%s]: ' % str(self.default),
                validators=[
                    util.Validator(util.is_number),
                    util.Validator(util.number_in_range, (0, len(self.items)))
                ])

            sel = int(inp) if inp else self.default
            self.print_selected(sel)
            self.selection = self.items[sel]
            break
        # return self.execute_or_return()

    def run_or_return(self):
        if isinstance(self.selection, FunctionItem):
            return self.selection.call_func()
        if isinstance(self.selection, ValueItem):
            return self.selection.value

    def menu_validation(self):
        try:
            int(self.default)
        except ValueError:
            print('Default value: "%s" is not a number' % self.default)
            return False
        if len(self.items) < 1:
            print('There are no items to choose from!')
            return False
        if self.default not in range(0, len(self.items)):
            print('Default value not in item list!')
            return False
        return True

    def get_max_label_length(self):
        return max(len(i.label) for i in self.items)


def main():
    menu_items = [FunctionItem('Exit', exit, ['Terminating script']),
                  ValueItem('a', 'qs'),
                  ValueItem('P', 'prod')]
    m = Menu(menu_items, 1)
    m.select()
    print(m.run_or_return())


if __name__ == '__main__':
    main()
