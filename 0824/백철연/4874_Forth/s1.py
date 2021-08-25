import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    Forth = list(map(str,input().split()))
    print(Forth)
    cal = ['*','/','-','+']
    stack = []

    for i in Forth:
        if i in cal:
            