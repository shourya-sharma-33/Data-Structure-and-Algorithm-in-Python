nn= [5,7,7,7,7,3,2,6,1,5,9]
nums = nn

def func(nums):
    n = len(nums)
    temp = nums[n-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    return nums

print(func(nums))