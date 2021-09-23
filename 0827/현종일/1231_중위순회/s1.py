import sys
sys.stdin = open("input.txt")

def in_order(n):
    if n:
        in_order(left[n])
        print(char_list[n], end="")
        in_order(right[n])

for tc in range(1, 11):
    V = int(input())
    char_list = [0]
    left = [0] * (V+1)
    right = [0] * (V+1)
    for i in range(1, V+1):
        temp = input().split()
        temp.pop(0)
        char_list.append(temp.pop(0))
        while temp:
            if left[i] == 0:
                left[i] = int(temp.pop(0))
            else:
                right[i] = int(temp.pop(0))
    print('#{} '.format(tc), end="")
    in_order(1)
    print()
