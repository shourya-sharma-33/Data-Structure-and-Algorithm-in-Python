result = []
def factor(num):
    for i in range(1, num+1):
        if num % i == 0 :
            result.append(i)
    return result

print(factor(69))
