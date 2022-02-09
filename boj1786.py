import sys
input = sys.stdin.readline

def get_pi(pattern): #Pi배열, LPS
    length = len(pattern)  # 패턴의 길이
    lps = [0] * length  # Pi 배열을 저장할 공간
    
    p_idx = 0  # 패턴의 인덱스
    for idx in range(1, length):  #파이 배열의 첫 값은 0임
        #p_idx가 0이 되거나, idx와 p_idx의 접근 값이 같아질 때 까지
        while p_idx > 0 and pattern[idx] != pattern[p_idx]:
            #p_idx가 0보다 크고 idx와 p_idx의 접근 값이 다를 때
            p_idx = lps[p_idx-1]  # 줄여서 계속 탐색
        
        if pattern[idx] == pattern[p_idx]:
            p_idx += 1  # 값이 일치하면 그 값을 저장
            lps[idx] = p_idx
    return lps

def KMP(word, pattern):
    lps = get_pi(pattern)  # 파이 배열 가져오기
    
    result = []
    p_idx = 0
    
    for idx in range(len(word)):
        while p_idx > 0 and word[idx] != pattern[p_idx]:
            p_idx = lps[p_idx-1]
        if word[idx] == pattern[p_idx]:
            if p_idx == len(pattern)-1:
                result.append(idx - len(pattern)+2)
                p_idx = lps[p_idx]
            else:
                p_idx += 1
    return result

word = input().rstrip()
pattern = input().rstrip()
result = KMP(word,pattern)
print(len(result))
for num in result:
    print(num)