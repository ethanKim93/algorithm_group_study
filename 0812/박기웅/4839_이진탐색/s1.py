import sys
sys.stdin = open("sample_input.txt")

def binary_search(P, key):
    l, r, c = 1, P, int((1+P)/2) #왼쪽, 오른쪽, 중간 page 초기화
    cnt = 0
    while(c!=key): #중간값이 찾는 값이면 종료
        c = int((l+r)/2) #중간값 갱신
        if (c == key):
            break
        elif( c > key ):
            r = c #중간값이 찾는 값보다 크면 오른쪽을 중간 값으로 갱신
            cnt += 1 #검색수 1번 추가
        else:
            l = c
            cnt += 1
    return cnt

for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    if binary_search(P, A) < binary_search(P, B):
        win = 'A'
    elif binary_search(P, A) > binary_search(P, B):
        win = 'B'
    else:
        win = '0'

    print('#{} {}'.format(tc, win))


