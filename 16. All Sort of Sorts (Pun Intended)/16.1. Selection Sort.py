n = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]
nums = n
def sort(nums):  # defining sorts with array variable num
    n = len(nums)  # length
    for i in range(0,n): # we will run this loop for each index, i is pointer
        min_index = i     # for a specific loop, we asign it a variable
        for j in range(i+1,n): # for i pointing at any element of array
                                          # a pointer j goes to all elements after i
                                          # if nums[j] < nums[min_index] then we replace i and j, and continue
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

print(sort(n))

# time complexity is n sqared
# space complexity is 1
