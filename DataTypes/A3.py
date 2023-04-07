a = 5
b = 6
c = 2


def max_ele(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


max_abc = a if (a > b and a > c) else (b if (b > c and b > a) else c)

ans = max_ele(a, c, b)
print(ans)
print(max_abc)
