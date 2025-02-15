#!/usr/bin/python3
"""add item"""
import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, filename)
