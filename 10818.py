'''

max 값 min 값 구하기

'''

N = int(input())
#N =5

#num = '20 10 35 30 7'


num = list(map(int,input().split()))
print(min(num),max(num))