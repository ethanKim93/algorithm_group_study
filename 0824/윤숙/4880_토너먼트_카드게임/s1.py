import sys

sys.stdin = open('input.txt')
T = int(input())
winidx=0

def game(p1, p2):
    #  1 가위 2 바위 3 보
    if p1 == 1 and p2 == 2:
        return p2
    elif p1 == 1 and p2 == 3:
        return p1
    elif p1 == 2 and p2 == 1:
        return p1
    elif p1 == 2 and p2 == 3:
        return p2
    elif p1 == 3 and p2 == 1:
        return p2
    elif p1 == 3 and p2 == 2:
        return p1
    else:
        return p1

def isWinner(team):
    while len(team) > 1:
        gameresult = []
        for i in range(len(team)):
            if len(team)==1:
                break
            if i+1 < len(team):
                gameresult.append(team.pop(0))
                gameresult.append(team.pop(0))
                if i + 1 < len(gameresult):
                    result = game(gameresult[i], gameresult[i + 1])
                gameresult.clear()
                team.insert(0, result)

    return team

for tc in range(1, T + 1):
    N = int(input())
    player = list(map(int, input().split()))


    team1 = player[0:len(player) // 2]
    team2 = player[len(player) // 2:len(player)]



    left=isWinner(team1)
    right=isWinner(team2)
    lt = ''.join(map(str,left))
    rt = ''.join(map(str, right))
    result=game(int(lt),int(rt)) # 게임 결과를 구해버림..;;;
    idx=player.index(result)+1  # 임시방편으로 인덱스를 찾는 걸 구햇는데 출력은 같은데 fail
    print('#{} {} '.format(tc, idx)) #이길 때 인덱스를 구하는 걸로 다시 짜야한다.
