# Method 1
def f(x):
    count = 0
    while x > 0:
        x = x//10
        count+=1
    return count

# time complexity depends on length of integer
print(f(34523233))


# Method 2

# Concept :
# non decimal part of log base 10 of any number added one  is no of digit
import math

def f2(x):
    if x == 0:
        return 1
    return math.floor(math.log10(x)) + 1
# time complexity is O(1)
print(f2(34523233))