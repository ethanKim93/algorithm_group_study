import sys
sys.stdin = open('sample_input.txt')


def check_bracket(test_sample):
    test_stack = []
    for i in range(len(test_sample)):
        if test_sample[i] == '(' or test_sample[i] == '{':
            test_stack.append(test_sample[i])
        elif test_sample[i] == ')':
            if len(test_stack) == 0 or test_stack.pop() != '(':
                return 0
        elif test_sample[i] == '}':
            if len(test_stack) == 0 or test_stack.pop() != '{':
                return 0
        if len(test_sample)-1 == i:
            if len(test_stack):
                return 0
            else:
                return 1


T = int(input())
for tc in range(1, T+1):
    test_sentence = input()
    answer = check_bracket(test_sentence)

    print('#{} {}'.format(tc, answer))
