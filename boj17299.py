import sys
from collections import Counter
input = sys.stdin.readline


n = int(input().rstrip())
nums = list(map(int,input().split()))
cnt_nums = dict(Counter(nums)) # 숫자의 갯수로 딕셔너리 만들기
#print(cnt_nums)
# for cnt in nums: 
#     cnt_nums.append(nums.count(cnt))
stack = [0]
result = [-1] * n


for idx in range(1, n):
    while stack:  # 스택에 존재하면
        if cnt_nums[nums[idx]] > cnt_nums[nums[stack[-1]]]:  #인덱스에 해당하는 숫자가 최상위스택보다 크다면
            result[stack.pop()] = nums[idx]
        else:  # 크지 않으면
            stack.append(idx)
            break
            
    
    if not stack:  # 스택에 없으면 추가
        stack.append(idx)

print(*result)