
phone_book = ["119", "97674223", "1195524421"]
phone_book=["12","123","1235","567","88"]

phone_book = ["123","456","789"]
result = True

# for i in range(len(phone_book)):
#     if result == False:
#         break
#     for j in range(i,len(phone_book)):
#         if i != j:
#            print(phone_book[i],phone_book[j])
#            if phone_book[i] in phone_book[j]:
#                result = False
#                break

# print(result)
result = True

phone_book = sorted(phone_book)
for i in range(len(phone_book)-1):
    if phone_book[i] in phone_book[i+1]:
        result = False
        break

print(result)



a=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
# 0 0 0 1 0 2 0 3
# 1 0 1 1 1 2 1 3

print(a[:len(a)//2][:len(a)//2])
print(a[0][:2])
print(a[len(a)//2:])

print(a[:len(a)//2][:len(a)//2])