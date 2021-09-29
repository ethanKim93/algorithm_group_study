import sys
sys.stdin = open("input.txt")

temp = list(input())
byte_arr = []

while temp:
    tmp = []
    for _ in range(7):
        tmp.append(temp.pop(0))
    byte_arr.append(tmp)


for j in byte_arr:
    result = 0
    for idx, k in enumerate(j):
        if k == '1':
            result += 2**(6-idx)
    print(result, end=" ")

