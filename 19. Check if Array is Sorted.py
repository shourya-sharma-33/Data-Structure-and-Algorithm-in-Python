nn= [5,7,3,2,6,1,5,9]
nums = nn

def if_sorted(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True


print(if_sorted(nums))
