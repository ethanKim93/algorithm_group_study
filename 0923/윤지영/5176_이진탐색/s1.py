import sys
sys.stdin = open("5176_sample_input.txt")

# 중위순회식으로 순회
def inorder(n):
    global cnt
# 자연수 1부터 N까지의 수를 트리에 저장해야하므로 n이 N보다 작거나 같은 경우만 함수 실행
    if n <= N:
# 왼쪽 자식노드
        inorder(2*n)
# 부모 노드
        cnt += 1
        result[n] = cnt
# 오른쪽 자식노드
        inorder(2*n+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
# 트리에 넣을 값을 cnt = 0 으로 초기화
    cnt = 0
# tree를 result라는 list로 초기화
    result = [0] * (N+1)
# 1부터 순회 시작
    inorder(1)
    print('#{} {} {}'.format(tc,result[1], result[N//2]))