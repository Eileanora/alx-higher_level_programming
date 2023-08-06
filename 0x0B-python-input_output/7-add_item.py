#!/usr/bin/python3
"""Module that adds all arguments to a Python list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
MyList = []

try:
    MyList = load_from_json_file(filename)
except FileNotFoundError:
    pass

for i in range(1, len(sys.argv)):
    MyList.append(sys.argv[i])

save_to_json_file(MyList, filename)
