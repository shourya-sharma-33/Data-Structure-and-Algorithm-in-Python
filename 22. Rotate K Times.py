nn= [5,7,7,7,7,3,2,6,1,5,9]
nums = nn

# LOWKEY BRUTEFORCE

def func(nums,k):
    n = len(nums)
    rotation = k%n
    for i in range(0, rotation):
        e = nums.pop()
        nums.insert(0,e)

    return nums

print(func(nums, 4))

nums2 = nn
#  Better (using slicing)
def func2(nums,k):
    n = len(nums)
    k = n%k
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

print(func2(nums2,4))