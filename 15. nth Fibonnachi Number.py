# 0,1,1,2,3,5,8,13,21
# basically
# if fn is nth fibonnachi number
# f1 = 0
# f2 = 1
# f3 = 1 + 0 =1
# f4 = 1 + 1 = 2
# f5 = 2 +1 = 3
# f6 = 3 + 2 = 5
# f(n) = f(n-1) + f(n-2)
# f(0) = 0 and f(1) = 1

def f(n):
    if n ==0 or n==1:
        return n
    return f(n-1) + f(n-2) 
print(f(5))