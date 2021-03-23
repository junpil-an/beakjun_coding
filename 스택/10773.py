'''
입력한 값을 push 하고 0을 부룰 시 뒤에부터 하나씩 빼오는 알고리즘

'''

cnt=int(input())

empty = []

for i in range(cnt):
    num = int(input())

    if num == 0:
        
        if empty == []:
            empty.append(0)
        else:
            empty.pop()

    else:
        empty.append(num)

print(sum(empty))