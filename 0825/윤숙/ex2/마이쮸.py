# 받은 애는 줄선 수 만큼 받고
# 받은 애가 바로 줄서면 남은 애가 그뒤를 따로 들어가고
# 마지막에 받은 애가 누군지 판단
# 붕어빵문제와 유사하다고 함

mychu=20
person=1
mychu-=1
queue=[[person,1]]
while mychu>0:
    tmp=queue.pop(0)
    tmp[1]+=1
    mychu-=1
    queue.append(tmp)
    person+=1
    queue.append([person,1])
    print(queue)
print(queue[0][0])