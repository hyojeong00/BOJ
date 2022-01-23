n = int(input())
number = 1
cnt = 0

for i in range(1,n+1):
    number *= i

number = str(number)
# print(number[::-1])
for i in number[::-1]:
    if i=='0':
        cnt+=1
    else:
        break

print(cnt)