def func(li):
    temp1 = li.copy()
    temp1.append([4, 4, 4])
    temp2 = []
    for i in temp1:
        temp = []
        temp.append(i[0])
        temp.append(i[0] ** 2)
        temp.append(i[0])
        temp2.append(temp)
    return li, temp1, temp2


li = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
ans = func(li)
for i in ans:
    print(i)
