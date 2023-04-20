path = "./popular-names.txt"

with open(path, "r") as f:
    l = f.readlines()

print(len(l))