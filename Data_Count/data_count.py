"""
This is a Python Snippet that filters data in a JSON file based on the gender the user inputs
It then outputs the number per each gender
"""

import json

user_input=str(raw_input("Enter Gender\n").title())

if user_input!="":
    with open('file.json')as json_data:
        data=json.load(json_data)
        count = 0
        for r in (data['Users']):
            if (r['gender'] == user_input):
                print r['id'],str(r['first_name']),str(r['last_name']),str(r['email'])
                count += 1

        print '\n'
        print 'The Number of '+user_input+' is',count
else:
    print("You must enter a gender!!")
