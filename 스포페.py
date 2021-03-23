'''3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00

'''
import sys

box= [0,0,24,60]


for i in range(int(sys.stdin.readline())):
    a=sys.stdin.readline()
    # 0 보다 클 경우
    if int(a[0:2]) >= box[0] and :
        box[0] = int(a[0:2])
        if int(a[3:5]) >= box[1]:
            box[1] = int(a[3:4])

    if int(a[8:10]) <= box[2]:
        box[2] = int(a[8:10])
        if int(a[11:13]) <= box[3]:
            box[3] = int(a[11:13])

if box[0] <= box[2] :
    print(''.join(str(box[0]).zfill(2)+":"+str(box[1]).zfill(2)+" ~ "+str(box[2]).zfill(2)+":"+str(box[3]).zfill(2)))
    if box[0] == box[2] and box[1] > box[3]:
        print(-1)
else:
    print(-1)

