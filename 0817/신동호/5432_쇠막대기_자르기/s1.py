import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    chains = input()
    chains = chains.split('()') #레이저 split
    plus = result = 0
    for chain in chains:
        minus = 0
        for c in chain: # split으로 나뉜 문자열들 각각에서 result에 지금까지 누적된 (의 개수 plus를 더해주고, )의 개수 minus를 나중에 plus에서 빼준다.
            if c == '(':
                plus += 1
            if c == ')':
                minus += 1
        result += plus
        plus -= minus
    print('#{} {}'.format(tc,result))
    # result = 0
    # pat = [1] * len(Chain)
    # for ind in range(1,len(Chain)):
    #     if Chain[ind] == '(':
    #         pat[ind] = pat[ind-1] + 1
    #     elif Chain[ind] == ')':
    #         pat[ind] = pat[ind-1] - 1
    # for ind in range(1,len(pat)-1):
    #     if (pat[ind] > pat[ind-1]) and (pat[ind] > pat[ind+1]):
    #         result += pat[ind]
    # print(pat, result)
    # 0 3 3 4 3 3 1