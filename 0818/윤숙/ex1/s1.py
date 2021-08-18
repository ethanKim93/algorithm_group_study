def stackPush(arr, M):
    global cnt
    check = isOverflow()
    if check == -1:
        return print('overflow')

    arr.insert(cnt, M)
    cnt += 1


def stackPop(arr):
    global cnt
    check = isUnderflow()
    if check == -1:
        return print('underflow')

    arr.pop(-1)
    cnt -= 1


def isOverflow():
    global cnt
    if cnt == n:
        return -1
    else:
        return 0


def isUnderflow():
    global cnt
    if cnt <= 0:
        return -1
    else:
        return 0


def CheckStack(arr):
    print(arr)


n = 10
cnt = 0
arr = []

stackPush(arr, 'A')
stackPush(arr, 'B')
stackPush(arr, 'A')
CheckStack(arr)
stackPop(arr)
stackPop(arr)
stackPop(arr)
stackPop(arr)
CheckStack(arr)
