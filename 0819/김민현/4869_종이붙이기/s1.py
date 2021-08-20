
import sys
sys.stdin = open("sample_input.txt")

for tc in range(1,int(input())+1):
    paper = int(input())
    p = 1
    n = paper // 10

    for i in range(1,n+1):
        if i%2:
            p = (p*2) - 1
        else:
            p = (p*2) + 1
    print('#{} {}'.format(tc,p))