import sys
sys.stdin = open("input.txt")

for tc in range(1,int(input())+1):
    word = [0]*5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
    print('#{}'.format(tc),end='')

    for i in range(max_len):
        for j in range(5):
            #1 허락받고 쓰자
            # if len(word[j]) > i:
            #     print(word[j][i],end='')
            #용서가 허락보다 쉽다.
            try:
                print(word[j][i],end='')
            except:
                pass
    print()

    N,K = map(int,input().split())

    #띠를 둘렀을 때
    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+1))
    ans = 0