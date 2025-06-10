num = [5,7,3,2,6,1,5,9]

n = num

#pointers
left = 0 
right = len(n) - 1

def func(num, left, right):
    if left > right:
        return
    num[left],num[right] = num[right],num[left]
    func(num, left +1, right -1)
    return num

print(func(n, left, right))

