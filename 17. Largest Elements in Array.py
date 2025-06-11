nn= [5,7,3,2,6,1,5,9]
nums = nn

# we will assign first number and find out the max of pointer and a pointer that iterates over all
# if number is larger we will reassign and keep going

def lar(nums):
    
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        largest = max(largest, nums[i])
    return largest

print(lar(nums))

