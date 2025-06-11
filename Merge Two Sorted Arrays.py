num1 = [1,3,4,6,7,8,9,12]
num2 = [1,1,4,6,8,9,9]

# we have to merge these to arrays and in the output array
#duplicates arent allowed in result array

n = len(num1)
m = len(num2)
result=[]
i=0
j=0

while i<n and j<m:
    if num1[i] <= num2[j]:
        if len(result)==0 or result[-1] != num1[i]:
            result.append(num1[i])
        i+=1
    else:
        if len(result)==0 or result[-1] != num2[j]:
            result.append(num1[j])
        j+=1
while i<n:
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        i += 1
while j >n:
        if len(result)==0 or result[-1] != num2[j]:
            result.append(num1[j])
        j+=1

print(result)