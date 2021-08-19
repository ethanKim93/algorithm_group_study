import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    sentence = list(input())
    bin_list=[]
    bin_list.append('1')

    for x in sentence :
        if x != bin_list[-1]:
            bin_list.append(x)
        else:
            bin_list.pop(-1)

    if len(bin_list[1:]) == 0 :
        result = 0
    else:
        result = len(bin_list[1:])

    print('#{} {}'.format(tc, result))