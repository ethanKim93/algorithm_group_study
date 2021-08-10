import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    N = int(input())
    blocks = list(map(int, input().split()))

    # N회 반복
    for n in range(N):

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


        # dump 진행 한 후의 , 최대 최소
        tall = blocks[0]
        small = blocks[0]
        for block in blocks[1:]:
            if block > tall:
                tall = block
            if block < small:
                small = block

        # N회 이내에 flat 해지면 종료
        if tall - small <= 1:
            break

    print('#{} {}'.format(tc, tall - small))

