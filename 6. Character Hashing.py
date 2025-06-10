string = "azyxyyzaaa"
cat = ["d","a","y","x"]
hashlist = [0]*26

for ch in string:
    aski = ord(ch)
    index = aski - 97
    hashlist[index] += 1

indexx = []
for ch in "abcdefghijklmnopqrstuvwxyz":
    indexx.append(ch)

len(indexx)
import pandas as pd
dictionary = pd.DataFrame(hashlist, indexx)
print(dictionary)