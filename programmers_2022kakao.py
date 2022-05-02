# def solution(id_list, report, k):
#     reports = {}
#
#     for rep in report:
#         f, t = rep.split()
#         if t not in reports:  # 신고 당한 사람이 목록에 없으면
#             reports[t] = {f: 1}  # f가 한 번 신고했음
#         else:  # 목록에 있으면
#             if f in reports[t]:  # 신고 한 사람이 또 신고한 경우
#                 if reports[t][f] == 0:
#                     pass
#                 else:
#                     reports[t][f] += 1
#                     if reports[t][f] >= 3:
#                         reports[t][f] = 0
#             else:
#                 reports[t][f] = 1  # 새로운 사람이 또 신고한 경우
#
#     suspects = []
#     for id in id_list:
#         if id in reports:
#             temp = 0
#             for x in reports[id].keys():
#                 temp += reports[id][x]
#             if temp >= k:
#                 suspects.append(id)
#
#     ans = [0] * len(id_list)
#     for idx in range(len(id_list)):
#         for rep2 in report:
#             f, t = rep2.split()
#             if f == id_list[idx] and t in suspects:
#                 ans[idx] += 1
#     return ans
from pprint import pprint


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2

report = set(report)
reports = {x: 0 for x in id_list}
ans = {x: 0 for x in id_list}
# 똑같은 딕셔너리를 두개 만들기
# reports = {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}
# ans = {'muzi': 0, 'frodo': 0, 'apeach': 0, 'neo': 0}

for rep in report:
    f, t = rep.split()  # from, to
    reports[t] += 1
    # 신고 당한 개수 세기

for rep in report:
    f, t = rep.split()
    if reports[t] >= k:
        ans[f] += 1
    # 신고 당한 사람의 누적 횟수가 k번 이상이면 신고한 사람의 딕셔너리에 +1
print(list(ans.values())) #딕셔너리의 값들만 리스트로 리턴


