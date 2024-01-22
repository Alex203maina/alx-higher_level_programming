#!/usr/bin/python3

def raise_exception():
    try:
        raise TypeError("This is a type of exception")
    except TypeError as e:
        print("Exception caught:", e)
