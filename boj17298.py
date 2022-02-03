import sys
input = sys.stdin.readline()

n = int(input().rstrip())
nums = list(map(int,input().split()))
stack = []

for i in range(n):
    while(stack):
        if nums[i] > nums[stack[-1]]:
            nums[stack.pop()] = nums[i]
        else:
            stack.append(i)
            break
    
    if not stack:
        stack.append(i)
for i in stack:
    nums[i] = -1
    
print(*nums)