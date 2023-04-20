s_1 = "paraparaparadise"
s_2 = "paragraph"

def make_n_gram_string(n, string):
    ans = []
    string = list(string.replace(" ", ""))
    for i in range(len(string)):
        ans.append(string[i:i+n])
    for i in ans:
        if len(i) != n:
            ans.remove(i)
    ans_2 = []
    for i in ans:
        ans_2.append("".join(i))
    return ans_2

X = set(make_n_gram_string(2,s_1))
Y = set(make_n_gram_string(2,s_2))


wa = X | Y
seki = X & Y
sa = X - Y

print(wa)
print(seki)
print(sa)

print(f"'se'はXに含まれているか？:{'se' in X}")
print(f"'se'はYに含まれているか？:{'se' in Y}")

