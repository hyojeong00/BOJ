n = int(input())
words = []
for _ in range(n):
    words.append(list(map(lambda x: ord(x) - 65, input())))  # 알파벳을 숫자로 바꾸어 인덱스로 쓸 수 있도록 함

alphabets = [0] * 26  # 각 알파벳의 자릿수 저장

for word in words:
    for idx, char in enumerate(word[::-1]):
        alphabets[char] += (10 ** idx)  # 자릿수만큼 더해주기

alphabets.sort(reverse=True)  # 내림차순 정렬
sum_value = 0
num = 9
for i in range(9):
    sum_value += num * alphabets[i]
    num -= 1

print(sum_value)