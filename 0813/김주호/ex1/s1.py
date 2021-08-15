st = "SSAFY"

#Swap
li = []
for i in range(len(st)):
    li.append(st[len(st) - 1 - i])

print("".join(li))

#Slice
print(st[::-1])