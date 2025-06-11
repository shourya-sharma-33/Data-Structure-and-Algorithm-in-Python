nn = [1,1,0,1,0,1,1,1,1,0,1,1]
nums = nn

# how many maximums are at the same time

def count_max_con(nums):
    count = 0
    max_count = 0

    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else :
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count)
    
print(count_max_con(nums))
