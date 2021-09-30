import sys
sys.stdin = open('input.txt')

n = list(map(int,input()))

i = 0
while i != len(n):
    sum = 0
    for a in range(7):
        sum += n[i]*(2**(6-a))
        i += 1
    print(sum)
