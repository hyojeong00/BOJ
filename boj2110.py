import sys
input = sys.stdin.readline

N, C = list(map(int, input().split()))  #집 개수 N, 공유기 C개

arr = [int(input().rstrip()) for _ in range(N)]  # 공유기 거리
arr.sort()  # 이분탐색을 위한 정렬
# [1, 2, 4, 8, 9]
# 두 공유기 사이의 최대 거리를 이분탐색으로
start = 1  # 가장 짧은 거리; 최소 거리
end = arr[-1] - arr[0]  # 가장 큰 값 - 가장 작은 값 차이; 최대 거리
result = 0

while(start <= end):
    mid = (start + end) // 2  # 가장 클수 있는 거리의 중간값 4
    cur = arr[0] # 첫번째 값부터 시작
    cnt = 1
    for i in range(1,len(arr)): # 두번째 공유기부터 마지막까지
        if arr[i] >= cur + mid:  # 두번째 값이 시작값+거리 보다 크면
            cur = arr[i]  # 공유기를 설치
            cnt += 1

    if cnt >= C:  # 갯수가 공유기 개수보다 많거나 같으면
        start = mid + 1 #차이를 키워주기
        result = mid  # 우리가 원하는 값이되면 start > end로 while문 종료
    else:  # 더 적게 설치되면
        end = mid - 1  # 차이를 줄여주기
        
print(result)

# N, C = list(map(int, input().split(' ')))  #집 개수 N, 공유기 C개

# arr = [int(input().rstrip()) for _ in range(N)]
# arr = sorted(arr)

# start = 0
# end = arr[-1] - arr[0]
# result = 0

# while(start <= end):
#     mid = (start + end) // 2
#     val = arr[0]
#     cnt = 1
#     for i in range(1,len(arr)):
#         if arr[i] >= val + mid:
#             val = arr[i]
#             cnt += 1
#     if cnt >= C:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1
        
# print(result)
# # import sys
# input = sys.stdin.readline

# N, C = list(map(int, input().split(' ')))

# arr = []
# for _ in range(N):
#     arr.append(int(input().rstrip()))
# arr = sorted(arr)
# start = 0
# end = arr[-1] - arr[0]
# result = 0

# while(start <= end):
#     mid = (start + end) // 2
#     val = arr[0]
#     cnt = 1
#     for i in range(1,len(arr)):
#         if arr[i] >= val + mid:
#             val = arr[i]
#             cnt += 1
#     if cnt >= C:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1
        
# print(result)