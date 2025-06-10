def f(x):
    while x >0:
        last_digit = x % 10
        print(last_digit)
        x = x//10

print(f(4323))

