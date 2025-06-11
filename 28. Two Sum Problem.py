## Brute Force

nn = [5,9,1,2,4,15,6,3]
nums = nn

def two_sum(nums, target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

print(two_sum(nums, 13))

# if you are doing DSA for quite a while then i am sorry to hurt yout eyes
# if you dont understand then time complexity is too muc

# we can use a hashmap for this purpose

# Aproach 2
def two_sum2(nums,target):
    n = len(nums)
    hashmap = {}
    for i in range(0, n):
        remaining = target - nums[i]
        if remaining in hashmap:
            return [hashmap[remaining],i]
        hashmap[nums[i]]=i


print(two_sum2(nums, 13))
