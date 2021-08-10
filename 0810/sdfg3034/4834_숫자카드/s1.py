import sys
sys.stdin = open('input.txt')

T=int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = input()
    count = [0]*10
    for i in cards:
        i = int(i)
        count[i] += 1
    max_count = 0
    max_num = 0
    for j in range(10)[::-1]:
        if count[j] > max_count:
            max_count = count[j]
            max_num = j

    print('#{0} {1} {2}'.format(test_case,max_num,max_count))
