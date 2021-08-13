import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())
numsys = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for _ in range(1, T+1):
    tc, nums = input().split()
    text = input().split()
    GNS = {}

    for num in text:                # text에서 하나씩 꺼냄
        if num in GNS:              # GNS 딕셔너리에 해당 항목의 개수 카운팅
            GNS[num] += 1
        else:
            GNS[num] = 1

    print('{}'.format(tc))          # input 들어올때 #이 붙어서 들어옴 주의
    for i in numsys:                # numsys에서 하나씩 꺼냄
        for j in range(GNS[i]):     # GNS 딕셔너리에서 key가 i일때의 value값만큼 반복하면서
            print(i, end=" ")       # i를 출력
    print()