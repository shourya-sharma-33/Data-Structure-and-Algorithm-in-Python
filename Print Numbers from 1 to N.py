# forward

def func(i,n):
    if n == 0:
        return
    print(i)
    func(i+1,n-1)

func(1,5)

# backward
print("-"*20)

def func2(i,n):
    if n == 0:
        return
    func2(i+1,n-1)
    print(i)

func2(1,5)
