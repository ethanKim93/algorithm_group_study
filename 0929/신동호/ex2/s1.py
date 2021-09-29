# 01D06079861D79F99F
# 0F97A3
num = list(input())

output = ""
for i in num:
    n16 = int(i, 16)
    for j in range(3, -1, -1):
        output += "1" if n16 & (1 << j) else "0"


for x in range(len(output)//7 + bool(len(output)%7)):
    print(int(output[7*x:7*x+7], 2), end=', ')