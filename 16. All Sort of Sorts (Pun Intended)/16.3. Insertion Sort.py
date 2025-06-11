nn = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]

nums = nn
n = len(nums)
for i in range(1,n): # for i (pointer) in range 1 to n
    key = nums[i]     # key is the value, we will store it
    j = i-1                  # we will assign j = i -1
    while j >= 0 and nums[j] > key: #here if key is less than j then we replace and keep going until we dont need
        nums[j+1] = nums[j]              
        j -= 1
    nums[j+1] = key

print(nums)


# [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]