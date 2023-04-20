s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
def mainas(num):
    return num-1
index = map(mainas, index)

ans = {}

s = s.split(" ")

for i in range(len(s)):
    if i in index:
        ans[s[i][0]] = i + 1
    else:
        ans[s[i][0:2]] = i + 1

print(ans)