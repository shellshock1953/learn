filename = "learning_python.txt"

with open(filename) as f:
    print(f.read())

with open(filename) as f:
    for line in f.readlines():
        print(line.rstrip())

with open(filename) as f:
    filelines = list()
    for line in f.readlines():
        filelines.append(line.rstrip())

print(filelines)
