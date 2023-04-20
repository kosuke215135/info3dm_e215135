import random

def TypoglycemiaPermalink(string):
    stirng_list = string.split(" ")
    ans = ""
    for i in stirng_list:
        if len(i) < 4:
            ans = ans + i + " "
            continue
        first_str = i[0]
        last_str = i[-1]
        middle_str_list = list(i[1:-1])
        random.shuffle(middle_str_list)
        middle_str = "".join(middle_str_list)
        ans = ans + first_str + middle_str + last_str + " "
    return ans


s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(TypoglycemiaPermalink(s))


        
