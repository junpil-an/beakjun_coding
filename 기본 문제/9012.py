'''
(   ) 의 갯수


'''

for _ in range(int(input())):
    
    cnt = 0
    bracket = input()
    for i in bracket:
        if i == '(':
            cnt +=1
        elif i == ')':
            cnt -= 1
        
        if cnt < 0:
            print('NO')
            break
    if cnt == 0:
        print("YES")
    elif cnt > 0:
        print("NO")
        
    