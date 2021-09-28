import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    tree = [0] + [input().split(' ') for i in range(N)]  # 트리
    postfix = []         # 후위표기식
    result = []         # 계산 결과를 담을 배열
    for i in range(N, 0, -1):
        if not tree[i][1].isdecimal():  # 배열에 연산자가 포함되어있을 때
            if tree[i][1] == '+':
                tree[i] = [i,int(tree[int(tree[i][2])][1]) + int(tree[int(tree[i][3])][1])]
            elif tree[i][1] == '-':
                tree[i] = [i,int(tree[int(tree[i][2])][1]) - int(tree[int(tree[i][3])][1])]
            elif tree[i][1] == '*':
                tree[i] = [i,int(tree[int(tree[i][2])][1]) * int(tree[int(tree[i][3])][1])]
            else:
                tree[i] = [i,int(tree[int(tree[i][2])][1]) / int(tree[int(tree[i][3])][1])]
    print('#{} {}'.format(int(tree[1][1])))
