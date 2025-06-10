# we will make a dictionary to store frequency

n = [6,5,7,7,7,8,2,1,1,1,1,1,4,1,4,4,4,6,9]
nums = n
frequency_map = dict()

for i in nums:
    if i in frequency_map:
        frequency_map[i] += 1

    else:
        frequency_map[i] = 1

print(frequency_map)


n2 = n
hashmap = dict()
for i in n2:
    hashmap[i] = hashmap.get(i,0) + 1
print(hashmap)
