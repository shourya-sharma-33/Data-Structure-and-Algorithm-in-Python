nn= [5,7,0,7,0,3,0,6,1,5,9]
nums = nn

def zero(nums):
    if len(nums) ==1 or 0:
        return
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i += 1
    if i == len(nums):
        return
    j = i + 1
    while j < len(nums):
        if nums[j] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j += 1
    return nums

print(zero(nums))