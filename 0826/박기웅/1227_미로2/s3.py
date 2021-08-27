import sys
sys.stdin = open("input.txt")

'''
Brute Force? DFS? , 지나간 길을 1로 표시하는 코드
'''
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def escape():
    stack = [[1, 1]]                    # 출발점
    while stack:
        i, j = stack.pop()              # 시작

        for k in range(4):              # 4방향 가능여부 체크
            ni, nj = i+di[k], j+dj[k]   # 새 좌표 갱신
            if ni in range(100) and nj in range(100):   # 좌표가 미로 안에 있으면
                nxt = miro[ni][nj]                      # 해당 좌표의 값을 뽑아 확인

                if nxt == '3':                          # 3이면 끝냄
                    return 1
                elif nxt == '1':                        # 1이면 막다른 길이므로 넘김
                    continue
                else:                                   # 0 인 경우 이므로 이 길을 1로 찍고
                    miro[ni][nj] = '1'
                    stack.append([ni, nj])              # 스택에 저장

    return 0

for _ in range(10):
    tc = int(input())
    miro = [list(input()) for _ in range(100)]

    print('#{} {}'.format(tc, escape()))