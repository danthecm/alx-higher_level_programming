#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except Exception as e:
        pass
    finally:
        if result:
            print("Inside result: {:f}".format(result))
        else:
            print("Inside result: {}".format(result))

safe_print_division(10, 5)