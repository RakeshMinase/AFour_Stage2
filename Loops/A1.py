ans = 0


def sum_of_first_n(n):
    temp = 0
    for i in range(1, n + 1):
        temp += i
    return temp


n_100 = sum_of_first_n(100)
print(n_100)

n_10 = sum_of_first_n(10)
print(n_10)
