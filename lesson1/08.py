def cipher(string):
    string_list = list(string)
    ans = ""
    N = 219
    for i in string_list:
        code = ord(i)
        if code >= 97 and code <= 122:
            code = N - code
        st = chr(code)
        ans += st
    return ans

print(cipher("paraparaparadise"))