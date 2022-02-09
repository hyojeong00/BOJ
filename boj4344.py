import sys
input = sys.stdin.readline

case = int(input().rstrip())  # 테스트케이스 갯수

for _ in range(case):
    n, *scores = list(map(int, input().split()))  #학생 숫자, 점수들
    avg = sum(scores) / len(scores)  # 학생 평균

    cnt = 0
    for score in scores:
        if score > avg:  # 평균 넘는 학생들 숫자 세기
            cnt += 1

    result = cnt / len(scores) * 100

    print(f'{result:.3f}%')
