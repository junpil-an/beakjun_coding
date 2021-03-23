'''

첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.


입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

4 3 6 8 7 5 2 1

'''


# sequence = [1,2,3,4,5,6,7,8]


# empty = []

# for i in range(8):
    
#     num = int(input())
    
#     for j in range(1,num+1):
#         #print('j' , j)
#         if j not in empty:
#             empty.append(j)
#             print('+')

#         elif num in empty:
#             true = True
#             while true:
#                 popped = empty.pop()
#                 #print('popped', popped)
#                 if popped == num:
#                     true = False
#                 print('-')
#             break


# print(sequence.pop())

# for i in range(len(sequence)):
#     poped = sequence.pop()
#     if poped == 4:
#         break

#     print(sequence)
#     print(poped)

from sys import stdin
#n = int(stdin.readline)

num = [4,3,6,8,7,5,2,1]
cnt = 1
stack = []
result = []

# num 에다 전부 넣어 주고

for i in num:
    # 4 1,2,3,4
    # 3
    while cnt <= i:
        stack.append(cnt)
        result.append('+')
        cnt+=1
        print(i,cnt)
    # pop 이 4 가 아니면
    # 조건문을 걸어도 그냥 하나가 빠짐
    if stack.pop() != i:

        print("NO")
    # 그렇지않으면 빼줌 
    else:
        result.append('-')
