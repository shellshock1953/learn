import json
filename = 'fav_number.json'

try:
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"your fav number is {number}")
except FileNotFoundError:
    number = input("Write your favourite number:")

    with open(filename, 'w') as f:
        json.dump(number, f)
        print("saved")
