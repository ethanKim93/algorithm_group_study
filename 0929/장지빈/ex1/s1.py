import sys
sys.stdin = open('input.txt')

li = list(map(int, input()))
for i in range(len(li)//7):
    tmp = []
    tmp1 = 0
    for j in range(i*7, (i+1)*7):
        tmp.append(li[j])
    for a in range(7):
        tmp1 += tmp[-a-1] * (2 ** a)
    print('#{}: {}'.format(i+1, tmp1))