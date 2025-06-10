nn = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]
nums = nn
n = len(nn)

for i in range(n-2, -1,-1): # we put pointer I before the index
    for j in range(0,i+1):    # a pointer i is at an element, now another pointer 
                                         # is going in on each element comparing element next to it
                                         # and swapping if needed
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]


print(nums)

#[1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]