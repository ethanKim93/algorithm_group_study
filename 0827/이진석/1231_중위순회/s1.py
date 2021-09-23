import sys
sys.stdin = open('input.txt')

def in_order(n):        # 중위 순회
    if n:
        in_order(left[n])
        print(tree[n][1],end='')    # 알파벳의 문자 출력
        in_order(right[n])
for tc in range(1, 11):
    N = int(input())
    tree = [[0]]        # 완전 이진 트리 , 0번을 비우기
    left = [0] * (N+1)  # 왼쪽 자식
    right = [0] * (N+1) # 오른쪽 자식

    for i in range(1,N+1):
        temp = list(input().split(' '))
        tree.append([int(temp.pop(0)), temp.pop(0)])    # 노드 번호, 노드 알파벳 초기화
        if temp:                                        # 입력 문자열에서 알파벳 까지 pop됐을 때 남아있는 element가 있으면 왼쪽 자식이므로
            left[i] += int(temp.pop(0))                 # 왼쪽 자식 입력
        if temp:                                        # 마찬가지로 왼쪽 자식 입력 후에도 남아있다면
            right[i] += int(temp.pop(0))                # 오른쪽 자식 입력

    print('#{}'.format(tc),end=' ')
    in_order(1)
    print()