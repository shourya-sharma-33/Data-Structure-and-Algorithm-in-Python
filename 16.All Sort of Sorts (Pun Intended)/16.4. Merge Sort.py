nn = [1,3,5,2,4,1,4,1,3,9,7,6,8,5]
nums = nn

# lets make a function to merge sorted array

def merge_sorted_array(left, right): # left and right array 
    result = []
    i,j = 0,0
    n,m =len(left), len(right)
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if j >= m:
        while i <n:
            result.append(left[i])
            i +=1
    if i >=n:
        while j<m:
            result.append(right[j])
            j+=1
    return result

print("="*20)
print(merge_sorted_array([1,2,3,4,6,7],[3,4,5,8,9]))
#[1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]
print("="*20)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_sorted_array(left,right)
print("="*20)
print(merge_sort(nn))
print("="*20)