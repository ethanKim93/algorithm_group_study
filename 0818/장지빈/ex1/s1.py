import sys
sys.stdin = open('input.txt')


def stack_push(n):
    global ls
    ls.append(n)
def stack_pop():
    global ls
    if len(ls)==0:
        return False
    else:
        return ls.pop()

ls = []

stack_push('a')
print(ls)
stack_push('b')
print(ls)
stack_push('c')
print(ls)
print('')
stack_pop()
print(ls)
stack_pop()
print(ls)
stack_pop()
print(ls)
print('')
stack_pop()
print(ls)
print(stack_pop())
