li = ["abc.py", "abc.txt", "pqr.py", "pqr.txt", "asd.py", "xyz.txt"]

ans = [t for t in li if t[-4:] == ".txt"]
print(ans)
