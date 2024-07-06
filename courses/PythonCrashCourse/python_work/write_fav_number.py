import json
filename = 'fav_number.json'

number = input("Write your favourite number:")

with open(filename, 'w') as f:
    json.dump(number, f)
