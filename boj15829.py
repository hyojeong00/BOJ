# H = (∑ i=0 부터 (l−1) 까지 ai * r^i) mod M
n = int(input())
word = input()
r = 31
m = 1234567891
result = 0

for i in range(len(word)):
    num = ord(word[i]) - 96
    result += num * (r ** i)

print(result % m)

