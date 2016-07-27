'''
This is a Python Snippet that filters data in a JSON file based on the ID the user inputs
Outputs them vertically
'''
import json

user_input=int(raw_input("Enter ID\n"))

if user_input!=0:
    with open('file.json') as json_data:
        data=json.load(json_data)
        for r in (data['Users']):
            if (r['id'] == user_input):
                print (r['id'])
                print (r['first_name'])
                print (r['last_name'])
                print (r['email'])
                print (r['gender'])
else:
    print("ID must enter a number")
