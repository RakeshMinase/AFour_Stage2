def sum_of_n_cubes(n):
    ans = 0
    for i in range(1, n + 1):
        ans += i * i * i
    return ans


ans = sum_of_n_cubes(20)

print(ans)
