# Concept

# say a funtion exits such tha
# f(x) = 1 + 2 + 3 + 4 + 5 + 6 ......
# we can write the funtion as f(x) = x + f(x-1)
# and we can find all f of x by knowing a base value f(1) = 1
# lets see how we do it in python

def func(n):
    if n ==1:
        return 1
    return n + func(n-1)

print(func(10))
