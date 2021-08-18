import sys
sys.stdin = open("input.txt")
'''
재귀함수 정의하여 N을 하나씩 줄여가면서 
리스트 a를 왼쪽/오른쪽에 [0]을 concat해서 원소를 더하는 연산 
'''
def pascal_tri(N, a):
    print(*a)
    if N>1:
        pascal_tri(N-1,[l+r for l,r in zip([0]+a,a+[0])])

for tc in range(1, int(input())+1):
    N = int(input())
    print('#{}'.format(tc))
    pascal_tri(N,[1])
