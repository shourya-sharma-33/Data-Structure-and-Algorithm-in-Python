# Lets take a string

string = "abcdeffedcba"
s = string
n = len(s)
#lets create pointers
right = n-1
left = 0

def func(s,left,right):
    while left <= right:
        if s[right] != s[left]:
            return "not palindrome"

        left += 1
        right-=1

    return "palindrome"

print(func(s, left,right))
