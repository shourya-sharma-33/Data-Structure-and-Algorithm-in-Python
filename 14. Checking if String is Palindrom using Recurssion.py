# in the last question, the code we wrote was taking too much space with variables, lets compress the code

def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left+1, right-1)

print("-"*20)
print(func(["abcdeffedcba"],0,len(["abcdeffedcba"])-1))
print("-"*20)
print(func(["bananaistasty"],0,len(["bananaistasty"])-1))
print("-"*20)