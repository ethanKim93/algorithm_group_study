import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    blocks = list(map(int, input().split()))

    # N회 반복
    for n in range(N+1):

        # 최대 최소 구하기
        tall = blocks[0]
        small = blocks[0]
        for block in blocks[1:]:
            if block > tall:
                tall = block
            if block < small:
                small = block

        # blocks 리스트 돌면서 제일 먼저 만나는 tall -> small 1블럭 이동
        for i in range(len(blocks)):
            if blocks[i] == tall:
                blocks[i] -= 1
                break
        for i in range(len(blocks)):
            if blocks[i] == small:
                blocks[i] += 1
                break

        # N회 이내에 flat 해지면 종료
        if tall - small <= 1:
            break

    print('#{} {}'.format(tc, tall - small))



# 가장 높은곳(여러개면 맨 앞) -1 가장 낮은곳(여러개면 맨 앞) +1 반복
# 가장 높 - 낮 차이가 1 이하이면 break
# 아니면 N회 반복