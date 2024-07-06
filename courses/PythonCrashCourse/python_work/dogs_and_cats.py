filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            print(f"{filename}:\n{f.read()}")
    except FileNotFoundError:
        # print(f"{filename} is missing")
        pass
