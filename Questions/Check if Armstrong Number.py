num = int(input("enter number"))
n = num # to keep the orignal number for comparision

nod = len(str(n)) # number of digit

total = 0

while n > 0:
    id = n % 10
    total = total + id**nod
    n = n//10
print(total == num)



