'''
This is a Python Snippet that sorts data in a JSON file based on the first_name
'''
import json

temp = []
dictList = []

with open('file.json') as data_file:
    data = json.load(data_file)
    s = sorted(data.keys())
    for key in s:
        print(key, data['Users'])