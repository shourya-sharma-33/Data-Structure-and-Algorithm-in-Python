num1 = [1,0,3,4] #4
num2 = [4,6,4,2,3,5,7,0,1] #9
num3 = [3,0,1] #3


# you have to find the solution of this problem
# constraint is that no duplicates
# we have to find between 0 to len(numx) what is missing, like in num3, from 0 to 3 what number is missing

#
#
# brute force
# iterate over each value and compare with numbers in range of the length
#

n2 = len(num2)

def brute_force(arr):
    for i in range(0,len(arr)+1):
        if i not in arr:
            return i

# but the time complexity is n square

#
#
# better solution
#
#

# we will construct a dictionary and store all number in range 0 to length of array
# and will change the value when a number is in the list, now whichever key has value
# of 0 we know its missing

freqmap={}
def dict_method(arr):
    for i in range(0, len(arr)):
        freqmap[i]= 0
    for num in arr:
        freqmap[num]+=1
    for k,v in freqmap.items():
        if v==0:
            return k


#
#
# Optimal
#
#
# its a very diffrent kinda solution, see what it does is it
# uses this technique

# if we have to find what number is missing between in a list
# what we can do we can simply sum all numbers in list and substract with the sum of list

def sum_to_n(n):
    return n*(n-1)/2

missing = sum_to_n(len(num3))-(sum(num3))

# time complexity 1






