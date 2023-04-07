li = [3, 4, 6, 7, 8, 9]

li_tu = [(n, n * n) for n in li]

print(li)

print(li_tu)

dic = {t[0]: t[1] for t in li_tu}

print(dic)
