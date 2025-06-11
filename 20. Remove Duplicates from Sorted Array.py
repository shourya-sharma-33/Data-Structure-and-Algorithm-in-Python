nn= [5,7,7,7,7,3,2,6,1,5,9]
nums = nn

def func(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0,n):
        freq_map[nums[i]] = 0
    j = 0
    for k in freq_map:
        nums[j] = k
        j += 1
    return nums
print(func(nums))