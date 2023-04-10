def func(a, b=10):
    return a + b


ans1 = func(5)
ans2 = func(5, 9)

print(ans1)
print(ans2)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a, *temp, b = li

print(a)
print(b)
print(temp)


def function(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))


function(name_1="Shrey", name_2="Rohan", name_3="Ayush")


def func2(**temp):
    for i in temp.items():
        print(i.key + " " + i.value)


di = {1: "a", 2: "b", 3: "c"}
print(di.items())

func2(di.items())

# **temp = di
# print(temp.items())
