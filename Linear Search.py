nums = [5,3,9,8,16,4,-10]
target = 9 # we have to find in list
# we will iterate over each value in list and check with a variable target we
# will create a variable which we have to find in array

n = len(nums)

for i in range(0, n):
    if nums[i] == target:
        print(i)
