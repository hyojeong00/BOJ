import itertools


def solution(nums):
    n = len(nums) // 2
    set_nums = set(nums)
    if len(set_nums) < n:
        return len(set_nums)
    else:
        return n

nums = [3,1,2,3]
print(solution(nums))
nums = [3,3,3,2,2,4]
print(solution(nums))
nums = [3,3,3,2,2,2]
print(solution(nums))