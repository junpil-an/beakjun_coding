'''
제곱의 합 의 최소값

11 = 3**2 + 1**1 + 1**1

11 = 2**2 + 2**2 + 1**1 + 1**1 + 1**1

이면 최솟값은 3개

'''
import math


# N = int(input())

# a =[] 
# b = 1
# while True:
#     if b**2 > N:
#         break
#     a.append(b**2)
#     b = b+1

# a = a[::-1]
# List_Num= 0
# cnt = 0
# while True:
#     if N - a[List_Num] < 0:
#         List_Num += 1
#     else:
#         N = N -a[List_Num]
#         cnt +=1
#         print(a[List_Num])
#     if N==0:
#         break
# print(cnt)

# inputNum = int(input())
# nc = [0] * (inputNum+1) 
# for i in range(1, inputNum+1):
#     nc[i] = i 
#     for j in range(1, i):
#         if (j * j) > i:
#             break 
            
#         nc[i] = min(nc[i], nc[i - j * j] + 1 )

# print(nc[inputNum])

n = 20
dp = [0] * (n+1)

a = [i**2 for i in range(1,317)]

for i in range(1,n+1):
    s=[]

    for j in a:
        if i<j:
            break
        s.append(dp[i-j])
    dp[i] = min(s) +1 