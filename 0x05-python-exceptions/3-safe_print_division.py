#!/usr/bin/python3

def safe_print_division(a, b):
        """Returns the division of a by b."""
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print("Inside result: None")
    else:
        print("Inside result: {}".format(result))
    finally:
        return result
