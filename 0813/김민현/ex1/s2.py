swap = 'algorithm'
temp = list(swap)

for i in range(len(temp)//2):
    temp[i],temp[len(temp)-1-i] = temp[len(temp)-1-i],temp[i]
for i in temp:
    print(i,end='')