#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """return a list of variables attributes and method in an object"""
    return dir(obj)
