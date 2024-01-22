#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
        """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end=" ")
                count += 1
    except (IndexError, ValueError):
        pass
    finally:
        print("")
        return (count)
