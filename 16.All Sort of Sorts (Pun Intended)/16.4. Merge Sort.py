nn = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]
nums = n

# lets make a function to merge sorted array

def merge_sorted_array(left, right): # left and right array 
    result = []
    i,j = 0,0
    n,m =len(left), len(right)
    while i<n and j<m:
        if left