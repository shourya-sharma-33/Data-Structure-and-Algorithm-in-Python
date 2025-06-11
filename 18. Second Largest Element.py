nn= [5,7,3,2,6,1,5,9]
nums = nn


def slar(nums):
    largest = -9999999999999999999999999
    slargest = -999999999999999999999999
    #idk why inf dont work

    n = len(nums)
    for i in range (0,n):
        largest = max(largest, nums[i])

    for i in range(0,n):
        if nums[i] > slargest and nums[i] != largest:
            slargest=nums[i]

    return slargest

print(slar(nums))
