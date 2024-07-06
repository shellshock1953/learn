import json
filename = 'fav_number.json'

try:
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"your fav number is {number}")
except FileNotFoundError:
    print(f"no such file: {filename}")
