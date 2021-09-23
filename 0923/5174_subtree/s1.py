
import sys
sys.stdin = open('sample_input.txt')

# 백철연
import sys
sys.stdin = open('sample_input.txt')

def preorder(node):
    global cnt
    if node == 0:
        return cnt
    cnt += 1              # 갯수를 한번 씩 증가시키면서 타깃 노드 아래의 서브트리를 전위 순회
    preorder(left[node])
    preorder(right[node])


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split()) #  E - 간선의 개수  N - 타깃 노드
    arr = list(map(int, input().split())) # 노드리스트
    left = [0]*(E+2)  # 왼 자식 (1번자식
    right = [0]*(E+2) # 오른 자식 (2번자식

    for i in range(0, len(arr), 2): # 짝수 인덱스가 그 서브트리의 부모노드
        pr, child = arr[i], arr[i+1] # pr - 부모  child - 자식
        if left[pr] : # 0이 아니면(이미 노드 값이 있으면)
            right[pr] = child # 오른 자식으로
        else:
            left[pr] = child # 없으면 왼자식으로
    # print(left)
    # print(right)
    cnt = 0
    preorder(N) # 순회 함수 호출
    print('# {} {}'.format(tc, cnt))