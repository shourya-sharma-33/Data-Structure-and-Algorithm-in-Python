def func(x):
    if x == 1 or x ==0:
        return 1
    return x*func(x-1)

print(func(5))