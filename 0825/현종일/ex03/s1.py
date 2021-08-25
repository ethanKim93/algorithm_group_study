
queue = [1]
chew = [0] * 21
line = [0] * 21
i = 2
while queue:
    if sum(chew)+ line[queue[0]] >= 19:
        print('20번째 마이쮸는 {}번 '.format(queue.pop(0)))
        break

    idx = queue.pop(0)
    chew[idx] += line[idx]+1
    line[idx] += 1

    print('줄선사람 : {}'.format(queue))
    for p, c in enumerate(chew):
        if p and c: print('[{}번:{}개]'.format(p,c), end = ' ')
    print('')
    print('현재 나눠준 마이쮸갯수 : {}'.format(sum(chew)))
    queue.append(idx)
    queue.append(i)
    i += 1
    input()