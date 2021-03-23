'''

3번째로 큰 수

'''
T = int(input())

for i in range(T):
    num = sorted(list(map(int,input().split())))
    print(num[-3])
     