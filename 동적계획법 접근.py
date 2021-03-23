'''
x 가 3으로 나누어 떨어지면 3으로 나눈다
x 각 2로 나누어 떨어지면 2로 나눈다
1 을 뺀다

1로 만들수 있는 최솟값
'''

x= 10
cnt = 0

# while True :
#     if x%3 == 0 :
#         cnt+=1
#         x = x//3
#         print(3,x)
#     elif x%2 == 0 :
#         cnt +=1
#         x = x//2
#         print(2,x)
#     elif x%2 != 0 and x%3 != 0 :
#         if x == 1:
#             break
#         cnt+=1
#         x -= 1 
#         print(1,x)

# print(cnt)
dp =[0,0,1,1]
N = 10

for i in range(4,N+1):
                
    dp.append(dp[i-1]+1)
    # i의 나머지 0 
    if i%2 == 0 :
                                   
        dp[i] = min(dp[i//2] + 1 ,dp[i])
    if i%3 == 0 :
                        
        dp[i] = min(dp[i//3] + 1 ,dp[i])

print(dp)


dp =[0,1,0]

for i in range(2,10):
    dp[i] = dp[i-2] + dp[i-1]
    dp.append(dp[i])

print(dp)

coin = [6, 4, 1]

def coinchange(change):
    for N in range(1,change+10):
        min = INF
        for i in range(len(coin)):
            if N >= coin[i]:
                ret = memo[N-coin[i]]
            if min > ret:
                min = ret
            

