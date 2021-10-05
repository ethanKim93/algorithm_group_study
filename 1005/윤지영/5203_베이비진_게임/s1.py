import sys
sys.stdin = open('sample_input (1).txt')

def check(li):
    counts = [0] * 10
    for l in li:
        counts[l] += 1
        if counts[l] >= 3:
            return True
    li = sorted(set(li))              # 1 2 2 3 같은 경우도 run으로 처리해주기 위해서 중복 제거(set)로 정렬하여 확인
    for k in range(len(li)-2):
        if li[k] +1 == li[k+1] and li[k+1] +1 ==li[k+2]:
            return True


T = int(input())
for tc in range(1,T+1):
    card = list(map(int,input().split()))
    player1 = []
    player2 = []
    result = 0
    for i in range(0,len(card)-1,2):
        player1.append(card[i])
        if len(player1) > 2 :
            if check(player1) is True:
                result = 1
                break

        player2.append(card[i+1])
        if len(player2) > 2 :
            if check(player2) is True:
                result = 2
                break

    print('#{} {}'.format(tc,result))

