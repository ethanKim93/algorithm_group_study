import sys
sys.stdin = open("GNS_test_input.txt")

for tc in range(1, int(input())+1):
    T, N = input().split()
    strs = list(input().split())
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    nums_dict = {} #딕셔너리 키로 인덱싱 Ex. ZRO : 0, ONE : 1, ...
    for i, num in enumerate(nums):
        nums_dict[num] = i
    cnt = [0]*10 # 카운팅배열 추가
    for str in strs:
        cnt[nums_dict[str]] += 1

    print(T)
    for i in range(10):
        print( (nums[i]+' ')*cnt[i], end='') #원소의 개수만큼 키를 출력


