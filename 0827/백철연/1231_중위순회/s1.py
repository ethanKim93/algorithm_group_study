import sys
sys.stdin = open("input.txt")

def inorder(n): # 중위 순회
    if n <= N:                  # 정점번호 안에서
        inorder(n*2)             #n의 왼쪽자식으로 이동
        print(node[n], end= '') # 알파뱃 출력
        inorder(n*2+1)          #n의 오른쪽자식으로 이동



for tc in range(1, 11):
    N = int(input())
    node = [0] * (N+1) # 알파벳을 인덱스 번호로 접근하기 위한 빈 리스트
    for i in range(N):
        lst = list(input().split())
        #print(lst)
        node[i+1] = lst[1] # 빈리스에 알파벳을 정점 번호와 맞춰 넣음
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print()


