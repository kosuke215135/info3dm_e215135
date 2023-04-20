path = "./popular-names.txt"

with open(path, "r") as f:
    l = f.readlines()

write_file = input()

def replace_tab(string):
    return string.replace("\t", " ")

with open(write_file, "w") as f:
    l = map(replace_tab, l)
    f.write(''.join(l))
