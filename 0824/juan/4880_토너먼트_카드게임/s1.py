T = int(input())

def winner(l,r):
    if (tournament[l-1] - tournament[r-1])%3 < 2:       # l번 선수가 낼 카드와 r번 선수가 낼 카드로 비교해서 이긴 선수번호 return
        return l
    return r

def vs(start, end):                                     # start번 선수부터 end번 선수 그룹을 반으로 나눌 함수
    if start == end:                                    # start와 end가 같아진 경우(반씩 나누다가 1명으로 좁혀진 경우)
        return start                                    # start or end 중 하나를 return

    left = vs(start, (start+end)//2)                    # 둘로 나눴을때 왼쪽 그룹을 vs함수에 인자를 start번 부터 (start+end)//2번 까지 
    right = vs((start+end)//2+1, end)                   # 오른쪽 그룹을 vs함수에 인자를 (start+end)//2+1번 부터 end번 까지 넣은 결과로 재귀 분할
    return winner(left, right)                          # left와 right에 값이 할당되었다면 winner함수의 인자로 각각 넣어서 winner함수 호출

for tc in range(1, T+1):
    N = int(input())
    tournament = list(map(int, input().split()))        # 1번~N번 선수가 낼 카드 리스트

    print('#{} {}'.format(tc, vs(1, N)))                # vs(1, N) 함수를 호출했을때의 반환값(최종 승자)을 출력 