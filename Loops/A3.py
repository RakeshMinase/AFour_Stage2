def t_multipliers_of_n(n, t):
    li = []
    for i in range(1, t + 1):
        li.append(n * i)
    return li


ans = t_multipliers_of_n(4, 10)
print(ans)
