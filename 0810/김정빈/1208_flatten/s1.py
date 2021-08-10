import sys
sys.stdin = open('input.txt')

for T in range(1,11):
    N = int(input()) #덤프 횟수
    dump = list(map(int,input().split()))
    cnt = N

    while cnt >= 0:
        


    print('#{} {}'.format(T, 'sample'))

    # for tc in range(1, 11):
    #     num = int(input())  # 덤프횟수
    #     Data = list(map(int, input().split()))  # 리스트들
    #     for i in range(num):  # 덤푸횟수까지 i를 돌아
    #         max_d, min_d = max(Data), min(Data)  # 최고값 최저값 구한후에
    #         index_max_d = Data.index(max_d)  # 최고값이 있는 인덱스찾아
    #         index_min_d = Data.index(min_d)
    #         Data[index_max_d] -= 1
    #         Data[index_min_d] += 1
    #     print('#%s %d' % (tc, max(Data) - min(Data)))