from menu import *


def main():
    menu_items = [FunctionItem('Exit', exit, ['Terminating script']),
                  ValueItem('a', 'qs'),
                  ValueItem('P', 'prod')]
    m = Menu(menu_items, 1)
    m.select()
    print(m.run_or_return())


if __name__ == '__main__':
    main()
