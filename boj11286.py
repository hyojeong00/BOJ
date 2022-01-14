import sys
input=sys.stdin.readline

import queue
q=queue.PriorityQueue()

n=int(input().rstrip())  # 연산의 개수 N

for i in range(n):
    x=int(input().rstrip())  # 연산 X 받아오기
    if x==0:  # x가 0이면 절댓값이 가장 작은것 반환
        if q.qsize()==0:  # 배열이 비어있는 경우
            print(0)  #0을 반환
        else:  # 0이 아니면
            print(q.get()[1]) # 값을 반환
    else:  # 배열에 넣는 연산
        q.put((abs(x),x))