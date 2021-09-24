import sys
sys.stdin = open('input.txt')

def postorder(v):
    if v >= N:
        return
    if tree[v][2] > 0 :
        postorder(tree[v][2])	# 왼쪽 자식
    if tree[v][3] > 0 :
        postorder(tree[v][3])	# 오른쪽 자식

    if tree[v][1] == '+':
        tree[v][1] = tree[tree[v][2]][1] + tree[tree[v][3]][1] # 왼쪽 노드와 오른쪽 노드 더하기
    elif tree[v][1] == '-':
        tree[v][1] = tree[tree[v][2]][1] - tree[tree[v][3]][1] # 왼쪽 노드와 오른쪽 노드 뺄셈
    elif tree[v][1] == '*':
        tree[v][1] = tree[tree[v][2]][1] * tree[tree[v][3]][1] # 왼쪽 노드와 오른쪽 노드 곱셈
    elif tree[v][1] == '/':
        tree[v][1] = tree[tree[v][2]][1] / tree[tree[v][3]][1] # 왼쪽 노드와 오른쪽 노드 뺄셈


for tc in range(10):  # 10개의 테스트 케이스
    N = int(input())  # 정점의 총 수
    tree = [[0] * 4 for _ in range(N + 1)]  # 1 인덱스부터 시작해서 N+1
    # 트리 입력
    for n in range(N):
        info = list(input().split())
        if info[1].isdigit():  # 숫자면
            tree[int(info[0])][1] = int(info[1])
        else:
            tree[int(info[0])][1] = info[1]  # 연산자
            tree[int(info[0])][2] = int(info[2])  # 왼쪽 자식
            tree[int(info[0])][3] = int(info[3])  # 오른쪽 자식

    postorder(1)
    print("#{} {}".format(tc+1, int(tree[1][1])))