def sortSentence(s: str) -> str:
    num = []
    for item in s.split():
        x = item[-1] + item[:-1]
        num.append(x)
        num.sort()
    f_list = ""
    for i in num:
        f_list = f_list + i[1:] + ' '
    return f_list.rstrip()

s = "is2 sentence4 This1 a3"
print(sortSentence(s))