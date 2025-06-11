nn = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]
nums = nn

def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j= high
    while i<j:
        while nums[i] <= pivot and i<= high -1:
            i += 1
        while nums[j] > pivot and j >= low +1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]


print(partition(nums, 0, len(nums)-1))