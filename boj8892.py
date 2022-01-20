def pal(word):  #팰린드롬 판정
    if len(word)<2:
        return True
    if word[0] != word[-1]:
        return False
    return pal(word[1:-1])
    

n = int(input())  #테스트케이스의 숫자 n
for i in range(n):
    m = int(input())
    li = []
    for j in range(m):
        li.append(input())
    
    li2 = []
    for i in range(len(li)):
        for j in range(len(li)):
            if i==j:
                pass
            else:
                li2.append(li[i]+li[j])  # 가능한 모든 조합 
    
    result=[]
    for i in li2:
        if pal(i)==True:
            result.append(i)  #팰린드롬이라면 result에 넣기
    
    if len(result)==0:
        print(0)  # 팰린드롬 없다면 0 출력
    else:
        print(result[0])  # 있다면 아무거나 출력