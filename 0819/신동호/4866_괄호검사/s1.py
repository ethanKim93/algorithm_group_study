import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def check(cs):
    st = []
    for c in cs:
        if c == '{' or c == '(':
            st.append(c)
        if c == '}':
            if not st:
                return 0
            elif st[-1] != '{':
                return 0
            st.pop()
        if c == ')':
            if not st:
                return 0
            elif st[-1] != '(':
                return 0
            st.pop()
    if not st:
        return 1
    return 0



for tc in range(1, T+1):
    codes = input()
    print('#{} {}'.format(tc,check(codes)))