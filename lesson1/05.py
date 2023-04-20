def make_n_gram_word(n, word):
    ans = []
    wrod = word.split(" ")
    for i in range(len(wrod)):
        ans.append(wrod[i:i+n])
    for i in ans:
        if len(i) != n:
            ans.remove(i)
    return ans

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
    

a = "I am an NLPer"

b = make_n_gram_word(2, a)
c = make_n_gram_string(2, a)

print(b)
print(c)

