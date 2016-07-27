'''
This is a Python Snippet that filters data in a JSON file based on the gender the user inputs
'''

import json

user_input=str(raw_input("Enter Gender\n").title())

if user_input!="":
    with open('file.json')as json_data:
        data=json.load(json_data)
        for r in (data['Users']):
            if (r['gender'] == user_input):
                print (r['id'],str(r['first_name']),str(r['last_name']),str(r['email']))
else:
    print("You must enter a gender!!")
