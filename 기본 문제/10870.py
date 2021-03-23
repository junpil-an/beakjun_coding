'''

n 번째 피보나치 수 출력


'''

n = int(input())

fibo = [0,1]

for i in range(2,n+1):
    num = fibo[i-2]+fibo[i-1]
    fibo.append(num)
if n == 0 :
    print(0)
else:    
    print(fibo[-1])
