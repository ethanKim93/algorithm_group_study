import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    pipe = input()

    left = right = cnt = razer = 0
    cut = '()'

    i = 0
    while i < len(pipe):
        if i == len(pipe) - 1:
            break
        else:
            if pipe[i:i+2] == cut:
                for j in range(i, len(pipe)-1, 2):
                    if pipe[j:j+2] == cut:
                        razer += 1
                    else:
                        break

                if left:
                    cnt += left * (razer + 1)
                    left = 0
                    i += razer * 2
                else:
                    if pipe[i+(razer * 2)] == ")":
                        for j in range(i+(razer * 2), len(pipe)):
                            if pipe[j] == ")":
                                right += 1
                            else:
                                break
                        cnt += right * (razer + 1)
                        i += right
                        right = 0
                        i += razer * 2

            else:
                left += 1
                i += 1
    print('#{} {}'.format(tc, cnt))