fibo = [0]  * 91

fibo[1] = 1
fibo[2] = 1

for idx in range(3,91):
    fibo[idx] = fibo[idx-2] + fibo[idx-1]

print(fibo[int(input())])