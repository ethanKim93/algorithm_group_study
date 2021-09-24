import sys
sys.stdin = open('sample_input.txt')

def subtree(N):
    global cnt
		# 부모 번호에 자식 번호가 있을 때까지 루프
    while nodes[N]:
				# 자식이 있으면 하나씩 빼서 재귀문으로 자식이 부모인 노드 확인
        n = nodes[N].pop()
        cnt += 1
        subtree(n)

for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split())) # 부모, 자식 쌍
    nodes = [[] for _ in range(E+2)] # 부모 인덱스에 자식 번호를 담을 2d list 선언
    cnt = 1  # 자신을 포함하므로 1부터 시작
    for i in range(E):
				# nodes의 인덱스가 부모노드의 번호, 부모 번호에 자식 번호를 append
        nodes[pairs[2*i]].append(pairs[2*i+1])
    subtree(N)
    print('#{} {}'.format(tc, cnt))