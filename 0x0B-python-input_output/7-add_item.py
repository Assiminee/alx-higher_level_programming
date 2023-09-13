#!/usr/bin/python3
""" add_item module
"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """ adds all arguments to a Python list,
    and then save them to a file
    """
    data = []
    try:
        obj = load_from_json_file("add_item.json")
        if len(argv) >= 2:
            data = obj + [argv[i] for i in range(1, len(argv))]
    except Exception:
        if len(argv) >= 2:
            data = [argv[i] for i in range(1, len(argv))]
    save_to_json_file(data, "add_item.json")


add_item()
