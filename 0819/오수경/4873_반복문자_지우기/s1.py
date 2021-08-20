import sys
sys.stdin = open('sample_input.txt')



def del_repeat(repeat_str):
    if len(repeat_str) <= 1:
        if len(repeat_str) == 1:
            return 1
        else:
            return 0

    else:
        stack.append(repeat_str[0])
        for word in repeat_str[1:]:
            if len(stack) != 0 and stack[-1] == word:
                stack.pop(-1)
            else:
                stack.append(word)
        return len(stack)



T = int(input())
for tc in range(1, T+1):
    repeat_str = input()
    stack = []
    print("#{} {}".format(tc, del_repeat(repeat_str)))