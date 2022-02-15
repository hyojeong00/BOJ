# N, C = list(map(int, input().split()))  # 집의 개수, 공유기의 개수

# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arr = sorted(arr)  # 이진탐색을 위해 정렬
# print(arr)

# start = arr[1] - arr[0]
# end = arr[-1] - arr[0]

# result = 0

# while (start <= end):
#     mid = (start + end) // 2  # 차이
#     val = arr[0]
#     cnt = 1
#     for i in range(1, len(arr)):
#         if arr[i] >= val + mid:
#             val = arr[i]
#             cnt += 1
#     if cnt >= C:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1

# print(result)
import sys
input = sys.stdin.readline

N, C = list(map(int, input().split(' ')))

arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))
arr = sorted(arr)
start = 0
end = arr[-1] - arr[0]
result = 0

while(start <= end):
    mid = (start + end) // 2
    val = arr[0]
    cnt = 1
    for i in range(1,len(arr)):
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1
    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)