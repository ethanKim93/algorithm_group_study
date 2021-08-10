import sys
sys.stdin = open("sample_input.txt")
for tc in range(1,int(input())+1):
    N = int(input())
    cards = input()
    cnt = {} #숫자 = key, 개수 = value
    for card in cards:
        try: cnt[int(card)] += 1
        except: cnt[int(card)] = 1

    maxn = maxc = -1 #음수로 변수 초기화 maxc = 숫자, maxn = 숫자 개수
    for key, val in cnt.items(): #숫자와 숫자 개수로 반복
        if maxn <= val: #숫자 개수가 크거나 같은 경우 maxn 갱신
            maxn = val
            if maxc < key: #큰 숫자 개수가 같은 경우 maxc 갱신
                maxc = key


    print('#{} {} {}'.format(tc, maxc, maxn))



