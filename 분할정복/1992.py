'''

홀수 번째와 짝수번째 의 합중 큰 합


'''

sticker=[14, 6, 5, 11, 3, 9, 2, 10,123, 12, 41,5,2,5,6,21,123]

odd = []
even = []
for i,s in enumerate(sticker):
    #print(i+1 ,s) 
    if (i+1)%2 == 0 :
        odd.append(s)
    else:
        even.append(s)
        
print(max(sum(odd),sum(even)))