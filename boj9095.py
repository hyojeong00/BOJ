import sys
input = sys.stdin.readline

test = int(input().rstrip())
nums = [1,2,4]

for i in range(3,10):
  nums.append(nums[i-3] + nums[i-2] + nums[i-1])

for i in range(test):
  n = int(input().rstrip())
  print(nums[n-1])
