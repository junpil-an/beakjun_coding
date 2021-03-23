'''
2개의 자연수를 받아 최대공약수 최소공배수

24 18

6 72
'''

import math

num1,num2 = map(int,input().split())

min = math.gcd(num1,num2)
max = num1*num2 // min

print(min)
print(max)
